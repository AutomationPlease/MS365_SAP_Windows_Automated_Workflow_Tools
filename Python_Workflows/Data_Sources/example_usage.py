# add at the top of each script that needs the data sources pulled in.

# my workflows are heavily involved in Windows and SAP applications. Annoyingly enough, they flip flop around needing the correct '\' or '/' or '\\' or '//'
# these can be adjusted for your specific needs are not necessary but for my workflows i've found this redundant setup works well.

import configparser
config = configparser.ConfigParser()
config.read(r"X:\Folder Name\Sub Folder Name\external_dataset.xlsx")
data_source_file_path = config['Paths']['data_source_file_path']
data_source_file_path = rdc_weekly_update_report_path.strip().strip('"').strip("'").lstrip('r').strip('"').strip("'")
data_source_file_path = rdc_weekly_update_report_path.replace('/', '\\')
