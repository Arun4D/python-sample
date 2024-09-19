import pandas as pd
import csv
import re

from . import helpers

class InputExcelData:
    def __init__(self, Source, Destination, Port):
        self.Source = Source
        self.Destination = Destination
        self.Port = Port
    
    # This function will be used to convert the class object into a dictionary for CSV export
    def to_dict(self):
        return {
            'Source': self.Source,
            'Destination': self.Destination,
            'Port': self.Port
        }

class OutputCSVData:
    def __init__(self, Source, Destination, Port):
        self.Source = Source
        self.Destination = Destination
        self.Port = Port
    
    # This function will be used to convert the class object into a dictionary for CSV export
    def to_dict(self):
        return {
            'Source': self.Source,
            'Destination': self.Destination,
            'Port': self.Port
        }

FIELD_MAPPING = {
    'Source': 'Source Criteria',
    'Destination': 'Destination Criteria',
    'Port': 'Port Criteria'
}

INPUT_EXCEL_COLUMNS_TO_READ = ['Source', 'Destination', 'Port'] 
INPUT_EXCEL_SECURITY_COLUMNS = ['Source', 'Destination'] 
INPUT_SERVICE_COLUMNS = ['Port'] 

# Step 2: Read Excel and store data into class objects
def read_excel_into_objects(file_path, columns):
    # Read the specific columns from Excel
    df = pd.read_excel(file_path, usecols=columns)
    
    # Store each row into a list of InputExcelData class objects
    data_objects = []
    for _, row in df.iterrows():
        # Create an instance of InputExcelData for each row
        column1 = convert_to_nst_format(row[columns[0]], columns[0])
        column2 = convert_to_nst_format(row[columns[1]], columns[1])
        column3 = convert_to_nst_format(row[columns[2]], columns[2])
        data_obj = InputExcelData(column1, column2, column3)
        data_objects.append(data_obj)
    
    return data_objects

def convert_to_nst_format(string_input, column_name):
    result = parse_key_value_string(string_input)
    
    prefix= ""
    if column_name in INPUT_EXCEL_SECURITY_COLUMNS:
        prefix= "SecurityGroup"
    elif column_name in INPUT_SERVICE_COLUMNS:
        prefix= "Service"

    result = parse_to_pipe_seperated(result, prefix)
    
    return result


def parse_key_value_string(s):
    # Regular expression to match 'key : value' patterns, with spaces around the colon
    pattern = r'(\S+)\s*:\s*(\S+)'
    
    # Find all key-value pairs
    matches = re.findall(pattern, s)
    
    # Convert the matches into a dictionary
    result = {key: value for key, value in matches}

    return result
    

def parse_to_pipe_seperated(input_dict, group_prefix):
    result = ""
    keys = ""
    values = ""
    for key, value in input_dict.items():
        keys = keys + group_prefix + ":"+key + "|" 
        values = values + group_prefix + ":"+value + "|" 
    result = keys+values
    if bool(result and result.strip()):
        return result[:-1]

    return result

    print(f"result  {result}")
        
    return result

# Step 3: Convert class objects to CSV
def write_objects_to_csv(data_objects, output_csv_path):

    # Get fieldnames from mapping
    fieldnames = [FIELD_MAPPING[attr] for attr in FIELD_MAPPING]

    # Open the CSV file for writing
    with open(output_csv_path, mode='w', newline='') as csv_file:
        # Define the fieldnames for CSV
        #fieldnames = ['Source Criteria', 'Destination Criteria', 'Servicess Criteria']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header (column names)
        writer.writeheader()
        
        # Write data rows
        for obj in data_objects:
            row = {FIELD_MAPPING[attr]: getattr(obj, attr) for attr in FIELD_MAPPING}
            writer.writerow(row)

# Step 4: Main function to call the operations
if __name__ == "__main__":
    # File paths and columns to read from the Excel file
    # Specify the input Excel template file path and output CSV template file path
    input_excel_path = helpers.get_input_excel_name()
    output_csv_path =  helpers.get_output_csv_name()

    # Read data from Excel into class objects
    data_objects = read_excel_into_objects(input_excel_path, INPUT_EXCEL_COLUMNS_TO_READ)
    
    # Convert the class objects into CSV format
    write_objects_to_csv(data_objects, output_csv_path)
    
    print(f"Data has been successfully written to {output_csv_path}")