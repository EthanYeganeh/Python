# This is the original work of Mohammadhassan Yeganeshenas with the student# of 041086643
import csv
from record import Record

class RecordService:
    """A class to handle operations related to records."""

    def __init__(self, file_path):
        """
        Initialize the RecordService.

        Args:
            file_path (str): The path to the CSV file containing records.
        """
        self.file_path = file_path
        self.records = self._read_data()

    def _read_data(self):
        """
        Read data from the CSV file and create Record objects. 

        Returns:
            list: A list of Record objects.
        """
        records = []
        try:
            with open(self.file_path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)
                for i, row in enumerate(csvreader):
                    record = Record(i + 1, *row)
                    records.append(record)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"An error occurred: {e}")
        return records

    def reload_data(self):
        """Reload data from the dataset."""
        self.records = self._read_data()
        print("data reloaded successfuly")

    def save_data(self, file_path):
        """
        Save records to a CSV file.

        Args:
            file_path (str): The path to save the CSV file.
        """
        try:
            with open(file_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['ID', 'Fiscal Year', 'Fiscal Period', 'Month', 'Information Date', 'Branch', 'Service', 'SSC Client', 'Metric Name', 'Value', 'Metric Type'])
                for record in self.records:
                    csvwriter.writerow([record.id, record.fiscal_year, record.fiscal_period, record.month, record.information_date, record.branch, record.service, record.sss_client, record.metric_name, record.value, record.metric_type])
            print("Data saved to file successfully.")
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")

    def display_records(self):
        """Display records to the console."""
        count = 0
        for record in self.records:
            print(f"Record {count + 1}:")
            print(f"ID: {record.id}")
            print(f"Fiscal Year: {record.fiscal_year}")
            print(f"Fiscal Period: {record.fiscal_period}")
            print(f"Month: {record.month}")
            print(f"Information Date: {record.information_date}")
            print(f"Branch: {record.branch}")
            print(f"Service: {record.service}")
            print(f"SSC Client: {record.sss_client}")
            print(f"Metric Name: {record.metric_name}")
            print(f"Value: {record.value}")
            print(f"Metric Type: {record.metric_type}")
            print("*******************************************************************")
            count += 1
            if count >= 100:
                break

    def add_record(self):
        """Add a new record."""
        new_id = len(self.records) + 1 
        fiscal_year = input("Enter Fiscal Year: ")
        fiscal_period = input("Enter Fiscal Period: ")
        month = input("Enter Month: ")
        information_date = input("Enter Information Date: ")
        branch = input("Enter Branch: ")
        service = input("Enter Service: ")
        ssc_client = input("Enter SSC Client: ")
        metric_name = input("Enter Metric Name: ")
        value = input("Enter Value: ")
        metric_type = input("Enter Metric Type: ")

        new_record = Record(new_id, fiscal_year, fiscal_period, month, information_date, branch, service, ssc_client, metric_name, value, metric_type)
        self.records.append(new_record)
        print("New record added successfully.")

    def edit_record(self, record_id):
        """Edit a record."""
        for record in self.records:
            if record.id == record_id:
                print("Record found:")
                print(f"ID: {record.id}")
                print(f"Fiscal Year: {record.fiscal_year}")
                print(f"Fiscal Period: {record.fiscal_period}")
                print(f"Month: {record.month}")
                print(f"Information Date: {record.information_date}")
                print(f"Branch: {record.branch}")
                print(f"Service: {record.service}")
                print(f"SSC Client: {record.sss_client}")
                print(f"Metric Name: {record.metric_name}")
                print(f"Value: {record.value}")
                print(f"Metric Type: {record.metric_type}")
                print("*******************************************************************")
                field_to_edit = input("Enter the field to edit (e.g., Fiscal Year): ")
                new_value = input(f"Enter the new value for {field_to_edit}: ")
                setattr(record, field_to_edit.lower().replace(" ", "_"), new_value)
                print("Record updated successfully.")
                return
        print("Record not found.")

    def delete_record(self, record_id):
        """Delete a record."""
        for index, record in enumerate(self.records):
            if record.id == int(record_id):
                del self.records[index]
                print("Record deleted successfully.")
                return
        print("Record not found.")
        
    def search_records(self, search_criteria: dict) -> list:
        """
        Search for the records inside the CSV file
        
        Returns: 
            The filtered records
        """
        filtered_records = []
        for record in self.records:
            match = True
            for column, value in search_criteria.items():
                record_value = str(getattr(record, column, "")).lower()
                if record_value != str(value).lower():
                    match = False
                    break
            if match:
                filtered_records.append(record)
        return filtered_records
