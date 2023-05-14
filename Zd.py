import pandas as pd

def read_excel(file_path):
    data = pd.read_excel(file_path)
    print(data)

# Usage
file_path = 'data.xlsx'  # Replace with your Excel file path
read_excel(file_path)
