import fitz
from PIL import Image
import os
import io
import sys

# output folder
output_folder = "images"
# make sure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# load the PDF
doc = fitz.open(sys.argv[1])

# iterate over PDF pages
for page_index in range(len(doc)):
    # get the page itself
    page = doc[page_index]
    # get the image list
    image_list = page.get_images(full=True)
    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    # iterate over the extracted images
    for image_index, img in enumerate(image_list, start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        image_filename = f"{output_folder}/img{page_index+1}_{image_index}.{image_ext}"
        image.save(open(image_filename, "wb"), format=image_ext.upper())
        # print the size of the image
        print(f"[*] Image {image_filename} saved, size: {image.size[0]} x {image.size[1]}")
