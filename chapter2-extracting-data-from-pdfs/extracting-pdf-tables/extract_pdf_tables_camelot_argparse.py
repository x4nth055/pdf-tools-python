import argparse
import camelot
import os

# Create the parser
parser = argparse.ArgumentParser(description='Extract tables from a PDF file.')
parser.add_argument('input_file', help='Input PDF file')
parser.add_argument('--extension', default='csv', choices=['csv', 'xlsx', 'html', 'zip'], help='Output file format')
parser.add_argument('--tables', default='all', help="Table numbers to extract, or 'all' to extract all tables")
parser.add_argument('--output', help='Pattern for output file names, without extension')
parser.add_argument("--output_folder", default="tables", help="Folder to store output files, default is 'tables'")

# Parse the command-line arguments
args = parser.parse_args()

# Create the output folder if it doesn't exist
if not os.path.exists(args.output_folder):
    os.makedirs(args.output_folder)

# Read the PDF file
tables = camelot.read_pdf(args.input_file)

# Determine the tables to extract
if args.tables == 'all':
    print(f"Total tables extracted: {tables.n}")
    tables_to_extract = range(tables.n)
else:
    tables_to_extract = [int(t) - 1 for t in args.tables.split(',')]
    
print(f"Tables to extract: {', '.join(str(i+1) for i in tables_to_extract)}")

# Determine the pattern for output file names
if args.output is None:
    output_base = os.path.splitext(args.input_file)[0]
else:
    output_base = args.output

# Extract the tables
for i in tables_to_extract:
    print(f"Extracting table {i+1} of {tables.n}...")
    if args.extension == 'csv':
        tables[i].to_csv(os.path.join(args.output_folder, f"{output_base}_table_{i+1}.csv"))
    elif args.extension == 'xlsx':
        tables[i].to_excel(os.path.join(args.output_folder, f"{output_base}_table_{i+1}.xlsx"))
    elif args.extension == 'html':
        tables[i].to_html(os.path.join(args.output_folder, f"{output_base}_table_{i+1}.html"))

# If 'zip' option is chosen, export all in a zip
if args.extension == 'zip':
    tables.export(os.path.join(args.output_folder, f"{output_base}_all.zip"), f="csv")

print(f"Successfully extracted tables: {', '.join(str(i+1) for i in tables_to_extract)} from '{args.input_file}' to '{args.extension}' format.")
