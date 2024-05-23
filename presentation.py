#This is the Original work of Mohammadhassan Yeganeshenas with the Student number: 041086643 
from business import RecordService
def get_search_criteria() -> dict:
            print("Enter the search criteria and type 'done' when finished")
            
            search_criteria= {}
            while True: 
                column = input("column to search: ").strip()
                if column.lower() == 'done':
                    break
                value = input(f"value for {column}: ").strip()
                search_criteria[column] = value
            return search_criteria

if __name__ == "__main__":
    # Initialize RecordService with the path to the CSV file containing records
    record_service = RecordService('enterprise-data-centres-en-november-2023.csv')

    # Main program loop
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Reload data from dataset")
        print("2. Save data to disk")
        print("3. Display records")
        print("4. Add a new record")
        print("5. Edit a record")
        print("6. Delete a record")
        print("7. Exit")
        print("8. Search")
        print("Mohammadhassan Yeganeshenas")  # Display full name
        
        # Prompt user for choice
        choice = input("Enter your choice: ")

        # Execute chosen action
        if choice == "1":
            record_service.reload_data()
        elif choice == "2":
            record_service.save_data('new_dataset.csv')
        elif choice == "3":
            record_service.display_records()
        elif choice == "4":
            record_service.add_record()
        elif choice == "5":
            record_id = int(input("Enter ID of the record you want to edit: "))
            record_service.edit_record(record_id)
        elif choice == "6":
            record_id = int(input("Enter ID of the record you want to delete: "))
            record_service.delete_record(record_id)
        elif choice == "8":
            criteria = get_search_criteria()
            matching_records = record_service.search_records(criteria)  
            if matching_records:  
                print("\nFound records matching your criteria:")
                for record in matching_records:
                    print("--------------------------------")
                    print(f"ID: {record.id}")  
                    print(f"Fiscal Year: {record.fiscal_year}")
                    print(f"Fiscal Period: {record.fiscal_period}")
                    print(f"Month: {record.month}")
                    print(f"Informattion date: {record.information_date}")
                    print(f"Branch: {record.branch}")
                    print(f"Service: {record.service}")
                    print(f"SSC Client: {record.sss_client}")
                    print(f"Metric Name: {record.metric_name}")
                    print(f"Value: {record.value}")
                    print(f"Metric Type: {record.metric_type}")
                    print("--------------------------------")
                    print("Programmed by Mohammadhassan Yeganeshenas")
                    
            else:
                print("No records found matching your criteria.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            

        