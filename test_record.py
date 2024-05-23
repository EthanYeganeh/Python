import unittest
from unittest.mock import patch
from record import Record
from DetailedRecord import DetailedRecord

class TestRecordPolymorphism(unittest.TestCase):
    """
    Unit tests for verifying polymorphism in Record and DetailedRecord classes through the display_record method.
    """
    
    def test_record_display(self):
        """
        Test the display_record method of the Record class for correct output format.
        """
        record = Record(1, "2023", "Q1", "January", "01/01/2023", "Finance", "Accounting", "ClientA", "Revenue", "10000", "Non-Cumulative")
        expected_output = "Record 1: Revenue - 10000"
        with patch('builtins.print') as mocked_print:
            record.display_record()
            mocked_print.assert_called_with(expected_output)
    
    def test_detailed_record_display(self):
        """
        Test the display_record method of the DetailedRecord class for correct detailed output format.
        """
        detailed_record = DetailedRecord(2, "2023", "Q2", "April", "04/01/2023", "HR", "Recruitment", "ClientB", "Hires", "5", "Cumulative")
        expected_output = "ID: 2, Fiscal Year: 2023, Metric: Hires, Value: 5"
        with patch('builtins.print') as mocked_print:
            detailed_record.display_record()
            mocked_print.assert_called_with(expected_output)

if __name__ == '__main__':
    unittest.main()
