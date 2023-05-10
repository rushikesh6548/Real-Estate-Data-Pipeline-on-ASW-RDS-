import os
import sys
import pandas as pd
# from src.logger import logging

class DataExtractionConfig():
    def __int__(self):
        if os.path.exists('all_data'):
            os.makedirs('all_data')
        self.raw_data_path = os.path.join('all_data','raw_data.csv')


class DataExtraction():
    def __int__(self):
        data_extraction_config_obj = DataExtractionConfig()
        self.raw_data_path = data_extraction_config_obj.raw_data_path

    def initiate_data_extraction(self):
        # logging.info("Initiated data extraction from API")
        # extracting all data from API from year
        # Getting the data from Data.gov :
        url = "https://data.ct.gov/api/views/5mzw-sjtu/rows.csv?accessType=DOWNLOAD"

        # data = pd.read_csv(url)
        # print(data)
        #
        # data.to_csv(self.raw_data_path)

        data = pd.read_csv(r"src/all_data/Real_Estate_Sales_2001-2020_GL.csv")
        print(data)


extraction_obj = DataExtraction()
extraction_obj.initiate_data_extraction()

