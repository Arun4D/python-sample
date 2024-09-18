from jproperties import Properties
from pathlib import Path
import os
 
configs = Properties()

with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

def get_input_excel_name(): 
    if is_input_excel_path_exists():
        if is_input_excel_name_exists():
            return str(configs.get("INPUT_EXCEL_PATH").data) + str(configs.get("INPUT_EXCEL_NAME").data)
        else:
            raise
    else:
        raise

def get_output_csv_name():
    output_file_name = str(configs.get("OUTPUT_CSV_PATH").data ) + str(configs.get("OUTPUT_CSV_NAME").data)
    if is_output_csv_path_exists():
        if is_output_csv_name_exists():
            return output_file_name
        else:
            path = Path(str(configs.get("OUTPUT_CSV_NAME").data))
            return output_file_name
    else:
        os.makedirs(str(configs.get("OUTPUT_CSV_PATH").data), exist_ok=True)
        path = Path(output_file_name)
        return output_file_name

def is_output_csv_name_exists():
    return is_file_exists(str(configs.get("OUTPUT_CSV_PATH").data + configs.get("OUTPUT_CSV_NAME").data))

def is_output_csv_path_exists():
    return is_path_exists(str(configs.get("OUTPUT_CSV_PATH").data))

def is_input_excel_name_exists():
    return is_file_exists(str(configs.get("INPUT_EXCEL_PATH").data + configs.get("INPUT_EXCEL_NAME").data))

def is_input_excel_path_exists():
    return is_path_exists(str(configs.get("INPUT_EXCEL_PATH").data))

def is_path_exists(path) :
    return os.path.exists(str(path)) 

def is_file_exists(file) :
    return os.path.isfile(str(file))
