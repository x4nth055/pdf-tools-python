import fitz
import sys

# get the PDF filename and password from the command line
pdf_filename = sys.argv[1]
password = sys.argv[2]
output_filename = "decrypted_" + pdf_filename

# open the PDF file
doc = fitz.open(pdf_filename)
# check whether the PDF file is encrypted
if doc.needs_pass:
    # authenticate the PDF file with the password
    result = doc.authenticate(password)
    if result == 0:
        print("Password incorrect!")
        sys.exit(1)
else:
    print("The PDF file is not encrypted.")
    sys.exit(1)
print("Password correct, decrypting...")
# save the PDF file without encryption
doc.save(output_filename)
