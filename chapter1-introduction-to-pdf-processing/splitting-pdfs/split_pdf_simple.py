import fitz
import sys
import os

# get the filename
pdf_filename = sys.argv[1]

# output folder
output_folder = "pages" # change this to your desired folder

# make the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# load the document
doc = fitz.open(pdf_filename)

for i in range(len(doc)):
    # make a new document
    new_doc = fitz.open()
    # insert the page
    new_doc.insert_pdf(doc, from_page=i, to_page=i)
    # save the document with a meaningful name
    new_doc.save(os.path.join(output_folder, f"{pdf_filename[:-4]}_page{i}.pdf"))
    