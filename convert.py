import pandas as pd

# Parameters
csv_file = 'parsedDataWLexer2.csv'
output_folder = '/Users/connor.neff/Desktop/Education/CSCE5290-NLPProject/'

chunksize = 50000  # Adjust this value based on your available memory

# Read the CSV file in chunks
reader = pd.read_csv(csv_file, chunksize=chunksize, iterator=True)
file_number = 1

for chunk in reader:
    # Save the current chunk to an Excel file
    output_file = f'{output_folder}excel_file_{file_number}.xlsx'
    chunk.to_excel(output_file, index=False, engine='openpyxl')
    print(f'Saved chunk {file_number} to {output_file}')
    file_number += 1

