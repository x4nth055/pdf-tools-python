import fitz
import sys
import os

# get the PDF file name from the command line
pdf_filename = sys.argv[1]
# open the PDF file
doc = fitz.open(pdf_filename)
# output file name based on the PDF file name
output_filename = os.path.splitext(pdf_filename)[0] + "_links.txt"
# set of links
all_links = set()
# iterate over PDF pages
for i in range(len(doc)):
    # get the Page object
    page = doc[i]
    # get the list of links
    links = page.get_links()
    # loop over the links
    for link in links:
        # get the link destination
        if "uri" in link:
            uri = link['uri']
            print(f"Page {i+1}:", uri)
            all_links.add(uri)
# write the links to the output file
with open(output_filename, "w") as f:
    for link in all_links:
        print(link, file=f)

        