import fitz
import sys
import os

# get the filename
pdf_filename = sys.argv[1]

# output folder
output_folder = "pages" # change this to your desired folder

# set of page numbers, each element is a list of individual page numbers
file_pages = [
    [0, 5, 6, 10],
    [12, 33, 50],
    [3, 9, 11, 14, 27, 39, 43, 51, 58],
]

# make the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# load the document
doc = fitz.open(pdf_filename)

for file_page in file_pages:
    # make a new document
    new_doc = fitz.open()
    # insert the page
    for page in file_page:
        new_doc.insert_pdf(doc, from_page=page, to_page=page)
    # save the document with a meaningful name
    new_doc.save(os.path.join(output_folder, f"{pdf_filename[:-4]}_pages{'-'.join([str(i) for i in file_page])}.pdf"))
    