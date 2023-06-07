import fitz
import argparse

# make the parser
parser = argparse.ArgumentParser(description='Merge PDF files')
# add the input PDFs argument
parser.add_argument('files', nargs='+', help='PDF files to merge')
# parse the arguments
args = parser.parse_args()

# create the new output PDF file
output_file = fitz.open()

# loop through the PDFs and add them to the output file
for pdf_file in args.files:
    print(f'Adding {pdf_file}')
    input_file = fitz.open(pdf_file)
    output_file.insert_pdf(input_file)

# save the output file    
output_file.save('merged.pdf')
