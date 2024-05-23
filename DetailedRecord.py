
from BaseRecord import BaseRecord

class DetailedRecord(BaseRecord): 
    """
    DetailedRecord is a subclass of BaseRecord that represents a more detailed version of a record.
    It extends the BaseRecord with the same attributes but overrides the display_record method to
    present a detailed view of the record's data.
    """
    def __init__ (self, id, fiscal_year, fiscal_period, month, information_date, branch, service, ssc_client, metric_name, value, metric_type):
        """
        Initializes a new instance of DetailedRecord with detailed information about a record.

        Args:
            id (int): The unique identifier for the record.
            fiscal_year (str): The fiscal year of the record.
            fiscal_period (str): The fiscal period of the record.
            month (str): The month associated with the record.
            information_date (str): The date of the information provided in the record.
            branch (str): The branch of service the record pertains to.
            service (str): The specific service within the branch.
            ssc_client (str): The SSC client associated with the record.
            metric_name (str): The name of the metric recorded.
            value (str): The value of the metric.
            metric_type (str): The type of metric (e.g., cumulative, non-cumulative).
        """
        super().__init__(id, fiscal_year, fiscal_period, month, information_date, branch, service, ssc_client, metric_name, value, metric_type)


    def display_record(self):
        """
        Displays a detailed representation of the record, including its ID, fiscal year, metric name, and value.
        Overrides the display_record method from BaseRecord.
        """
        print(f"ID: {self.id}, Fiscal Year: {self.fiscal_year}, Metric: {self.metric_name}, Value: {self.value}")