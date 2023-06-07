import fitz
import sys

# get the PDF filename and password from the command line
pdf_filename = sys.argv[1]
password = sys.argv[2]
# create the output filename
output_filename = "encrypted_" + pdf_filename
# open the PDF file
doc = fitz.open(pdf_filename)
# encrypt the PDF file
doc.save(output_filename, encryption=fitz.PDF_ENCRYPT_AES_256, owner_pw=password, user_pw=password)
