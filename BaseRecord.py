class BaseRecord:
    """
    A base class representing a generic record. This class provides the interface for displaying record details.
    Subclasses should implement the display_record method to specify how a record is displayed.
    """
    def __init__(self, id, fiscal_year, fiscal_period, month, information_date, branch, service, ssc_client, metric_name, value, metric_type):
        self.id = id
        self.fiscal_year = fiscal_year
        self.fiscal_period = fiscal_period
        self.month = month
        self.information_date = information_date
        self.branch = branch
        self.service = service
        self.ssc_client = ssc_client
        self.metric_name = metric_name
        self.value = value
        self.metric_type = metric_type

    def display_record(self):
        """
        Displays the record details. This method should be overridden by subclasses to provide specific
        implementation details on how the record is displayed.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("This Method must be overridden by subclasses")
