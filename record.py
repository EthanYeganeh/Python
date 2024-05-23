#This is the Original work of Mohammadhassan Yeganeshenas with the Student number: 041086643 
from BaseRecord import BaseRecord

class Record(BaseRecord): 
    """Data records with its attribute"""
    def __init__(self, id, fiscal_year, fiscal_period, month, information_date, branch, service, ssc_client, metric_name, value, metric_type):
        
        """ Initialize the Record Object"""
        self.id = id
        self.fiscal_year = fiscal_year
        self.fiscal_period = fiscal_period
        self.month = month
        self.information_date = information_date
        self.branch = branch
        self.service = service
        self.sss_client = ssc_client
        self.metric_name = metric_name
        self.value = value
        self.metric_type = metric_type
        
    def display_record(self): 
        """
        Displays the record in a predefined format, showcasing the metric name and its value.
        Overrides the display_record method from BaseRecord.
        """
        print(f"Record {self.id}: {self.metric_name} - {self.value}")
        
        