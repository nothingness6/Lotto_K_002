import unittest
from data.data_collector.py import DataCollector

class TestDataCollector(unittest.TestCase):
    def test_fetch_data(self):
        collector = DataCollector()
        data = collector.fetch_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
