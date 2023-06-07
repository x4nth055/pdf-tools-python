import argparse
import pdfplumber
import pandas as pd
import os

# Create the parser
parser = argparse.ArgumentParser(description='Extract tables from a PDF file.')
parser.add_argument('input_file', help='Input PDF file')
parser.add_argument('--extension', default='csv', choices=['csv', 'xlsx', 'all'], help='Output file format')
parser.add_argument('--output', help='Pattern for output file names')
parser.add_argument("--output_folder", default=".", help="Output folder for the converted files")

# Parse the command-line arguments
args = parser.parse_args()

# make sure the output folder exists
if not os.path.exists(args.output_folder):
    os.makedirs(args.output_folder)

with pdfplumber.open(args.input_file) as pdf:
    # iterate through the pages
    for i in range(len(pdf.pages)):
        # extract the page as a table
        table = pdf.pages[i].extract_table()
        if table is None:
            # skip the page if it does not contain any tables
            continue
        # convert it into a Pandas dataframe
        df = pd.DataFrame(table[1:], columns=table[0])
        # print the dataframe
        print(df)
        # Determine the output file names
        if args.output is None:
            output_base = os.path.splitext(args.input_file)[0] + f"_{i+1}"
        else:
            output_base = f"{args.output}_{i+1}"
        # Export the dataframe based on the specified format
        if args.extension in ['csv', 'all']:
            df.to_csv(os.path.join(args.output_folder, f"{output_base}.csv"))
        if args.extension in ['xlsx', 'all']:
            df.to_excel(os.path.join(args.output_folder, f"{output_base}.xlsx"))

print(f"Tables from '{args.input_file}' were successfully extracted and saved in '{args.extension}' format.")
