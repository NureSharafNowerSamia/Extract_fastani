import os
import pandas as pd

# Path of the output file

OUTPUT_FILE_PATH = r'path/to/.tsv'

# Path of the directories 'ARCH-BD\_0308'

INFO_DIRS_PATH = r'/path/to/phoenix/results/directory'

# Reads the csv output file

try:
df = pd.read_csv(OUTPUT_FILE_PATH)
# Sets the ID column as index column
output_df = df.set_index('ID')
except FileNotFoundError as e:
print(e)

def update_output(directory, extracted_value):
'''Updates the ANIm column of the output file with the extracted values
INPUTS:
directory: name of the current directory
extracted_value: value extracted from the input text file
OUTPUT: updated csv output file
'''
ids = output_df.index.to_list()
if directory not in ids:
raise ValueError(f'ID {directory} not found in the output file to update')
else:
output_df.loc[directory, 'ANIm'] = extracted_value

def extract_info(path):
'''Extracts the first line of required text file and update the output file
INPUT: info directories path.
OUTPUT: updated csv output file.
'''
for directory in os.listdir(path):

```
    # Get only the folders from specified directory
    if os.path.isdir(os.path.join(path, directory)):
        
        # Check if there is any path 'ANI\fastANI' inside the current directory
        if os.path.exists(os.path.join(path, directory, 'ANI//fastANI')):
            current_dir = os.path.join(path, directory, 'ANI//fastANI')
            filename = os.listdir(current_dir)[0]
            filepath = os.path.join(current_dir, filename)
            print(f'Now extracting info from {filepath}...')
            print(f'--------------------------------------')
            
            # Reading the files from every directory
            with open(filepath, 'r') as f:
                first_line = f.readline()
                extracted_value = first_line.strip()
                update_output(directory, extracted_value)
                
output_df.to_csv('output.csv')
```

if _name_ == '_main_':
extract_info(INFO_DIRS_PATH)

