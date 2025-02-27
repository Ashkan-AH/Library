import pandas as pd
import json


class BaseImportService:
    def __init__(self, data_file):
        self.data_file = data_file
        excel_data = pd.read_excel(data_file)
        data_json = excel_data.to_json(orient='records')
        self.data_list = json.loads(data_json)
        self.import_data()

    def import_data(self):
        pass
