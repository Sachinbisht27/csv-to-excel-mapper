import pandas as pd
from openpyxl import load_workbook

# File paths
csv_file = 'input.csv'
template_file = 'template.xlsx'
output_file = 'output.xlsx'

# Load CSV data using pandas
csv_df = pd.read_csv(csv_file)

# Load Excel template using openpyxl
workbook = load_workbook(template_file)
sheet = workbook.active  # Or use workbook['Sheet1'] if the sheet name is known

# Column mapping: CSV column -> Excel column letter
column_mapping = {
    'Name': 'A',
    'Email': 'B',
    'Age': 'C',
    'Department': 'D'
}

# Write data to Excel starting from row 2 (row 1 has headers)
start_row = 2

for i, row in csv_df.iterrows():
    for csv_col, excel_col in column_mapping.items():
        cell = f"{excel_col}{start_row + i}"
        sheet[cell] = row[csv_col]

# Save the populated Excel file
workbook.save(output_file)

print(f"Data successfully written to '{output_file}'")
