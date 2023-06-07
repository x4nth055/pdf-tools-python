from pdf2docx import Converter
import sys

# PDF file to be converted
pdf_file = sys.argv[1]
# Output docx file name
docx_file = sys.argv[2]

# create a Converter object
converter = Converter(pdf_file)

# convert the PDF file to a docx file
converter.convert(docx_file, start=0, end=None)

# close the Converter object
converter.close()