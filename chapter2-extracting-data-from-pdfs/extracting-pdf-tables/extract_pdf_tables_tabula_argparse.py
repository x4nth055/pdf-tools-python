import argparse
import tabula
import os

# Create the parser
parser = argparse.ArgumentParser(description='Extract tables from a PDF file.')
parser.add_argument('--input', help='Input PDF file')
parser.add_argument('--extension', default='csv', choices=['csv', 'xlsx', 'json', 'tsv'], help='Output file extension')
parser.add_argument('--pages', default='all', help="Page numbers to extract, or 'all' to extract all pages")
parser.add_argument('--output', help='Pattern for output file names')
parser.add_argument('--directory', help='Directory of PDFs to convert')
parser.add_argument('--single', action='store_true', help='Convert all tables of a PDF file into a ' \
                                                        'single file of the specified format by --extension argument')
# Parse the command-line arguments
args = parser.parse_args()
if args.input:
    # Read the PDF file
    tables = tabula.read_pdf(args.input, pages=args.pages)
    # Determine the pattern for output file names
    if args.output is None:
        output_base = os.path.splitext(args.input)[0]
    else:
        output_base = args.output
    # Convert all tables of a PDF file into a single file of the specified format by --extension argument
    if args.single:
        tabula.convert_into(args.input, f"{output_base}_all.{args.extension}", output_format=args.extension, pages=args.pages)
    else:
        # Extract the tables into separate files
        for i, table in enumerate(tables):
            if args.extension in ['csv', 'all']:
                table.to_csv(f"{output_base}_table_{i+1}.csv")
            if args.extension in ['xlsx', 'all']:
                table.to_excel(f"{output_base}_table_{i+1}.xlsx")
            if args.extension in ['json', 'all']:
                table.to_json(f"{output_base}_table_{i+1}.json")
if args.directory:
    # Convert all PDFs in a directory into single files of the specified format by --extension argument
    tabula.convert_into_by_batch(args.directory, output_format=args.extension, pages=args.pages)
