import fitz
import sys
import os

# input path
pdf_filename = sys.argv[1]
# output path
output_folder = sys.argv[2]
# make the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# read the PDF file
doc = fitz.open(pdf_filename)
# loop through the pages
for i in range(len(doc)):
    # get the page object
    page = doc[i]
    # render the page to a pixmap (a fitz.Pixmap object), which is an image representation
    pix = page.get_pixmap()
    # make the output filename
    output_filename = f"{pdf_filename[:-4]}_{i+1}.png"
    # the full path to the output file
    image_filename = os.path.join(output_folder, output_filename)
    # save the image as a PNG file
    pix.save(image_filename)
    # print a message to the user
    print(f"Page {i+1} saved as {output_filename}")
    
    