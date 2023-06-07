import fitz
import sys
import os

# get the filename
pdf_filename = sys.argv[1]

# output folder
output_folder = "pages" # change this to your desired folder

# set page numbers, each element is a tuple of (start_page, end_page) for each file
file_pages = [(0, 10), (10, 18), (18, 25), (25, 59)]

# make the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# load the document
doc = fitz.open(pdf_filename)

for file_page in file_pages:
    # make a new document
    new_doc = fitz.open()
    # insert the page
    new_doc.insert_pdf(doc, from_page=file_page[0], to_page=file_page[1])
    # save the document with a meaningful name
    new_doc.save(os.path.join(output_folder, f"{pdf_filename[:-4]}_pages{'-'.join([str(i) for i in file_page])}.pdf"))
    