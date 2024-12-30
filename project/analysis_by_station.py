import pandas as pd


class StationProcessor:
    def __init__(self, file_path, columns_of_interest):
        self.file_path = file_path
        self.columns_of_interest = columns_of_interest
        self.df = None

    def load_data(self):
        """Loads data from the given file path."""
        try:
            self.df = pd.read_csv(
                self.file_path,
                low_memory=False,
                date_format="mixed",
                parse_dates=["date"],
                usecols=self.columns_of_interest,
            )
        except Exception as e:
            print(f"Error loading data from {self.file_path}: {e}")
        return self.df

    def convert_knots_to_mps(self, data, column_name="wdsp"):
        """Converts wind speed from knots to m/s."""
        try:
            data[column_name] = data[column_name] * 0.514444
            data.rename(columns={column_name: "wdsp_mps"}, inplace=True)
        except Exception as e:
            print(f"Error converting wind speed for column {column_name}: {e}")
        return data
    
    import pandas as pd

    def fill_wind_speed_median(self, data, column_name="wdsp_mps"):
        """Fills missing values in the wind speed column with the median."""
        try:
            data[column_name] = pd.to_numeric(data[column_name], errors="coerce")
            median_value = data[column_name].median()
            data[column_name] = data[column_name].fillna(median_value)

            print(f"Missing values in '{column_name}' have been filled with the median: {median_value}")
        except Exception as e:
            print(f"Error processing column '{column_name}': {e}")
        
        return data


    def get_station_info(self, data):
        """Extracts and prints basic information about the dataset."""
        try:
            station_name = self.file_path.split("/")[-1].split("_")[0]
            print(f"Station Name: {station_name}")

            if "date" in data.columns:
                start_date = data["date"].min()
                end_date = data["date"].max()
                print(f"\nData Period: From {start_date.date()} to {end_date.date()}")
                print("\nDataset Overview:\n")
                data.info()

            print("\nSUMMARY:\n" + "---" * 10)
            summary_stats = data[["maxtp", "mintp", "rain", "cbl", "wdsp_mps"]].describe()
            print(summary_stats)

        except Exception as e:
            print(f"Error processing data: {e}")

    def run(self):
        """Runs the entire data processing workflow."""
       
        data = self.load_data()

        data = self.convert_knots_to_mps(data)

        data = self.fill_wind_speed_median(data)

        self.get_station_info(data)

        return data


