from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
from pypdf import PdfReader, PdfWriter

import argparse
from copy import deepcopy

# utility function to replace transparency with white background
def remove_transparency(img_path, output_path, bg_color=(255, 255, 255)):
    # open image
    img = Image.open(img_path)
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        # convert image to RGB if it is RGBA or LA
        alpha = img.convert('RGBA').split()[-1]
        bg = Image.new("RGB", img.size, bg_color + (255,))
        bg.paste(img, mask=alpha)
        # save image
        bg.save(output_path)
    else:
        img.save(output_path)
    print(f"[+] Transparency removed from {img_path} and saved at {output_path}")


def create_watermark_from_image(image_path, output_pdf_path=None):
    if not output_pdf_path:
        # if output_pdf_path is not provided, use the same name as image with pdf extension
        output_pdf_path = image_path.replace('.png', '.pdf')
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size
    # Create a canvas
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    # Calculate the x and y coordinates to center the image
    x = (letter[0] - img_width) / 2
    y = (letter[1] - img_height) / 2
    # Set the canvas fill color to white
    c.setFillColorRGB(1, 1, 1)  # RGB values range from 0 to 1
    # Draw a rectangle that covers the whole page
    c.rect(0, 0, letter[0], letter[1], fill=1)
    # Now the background is white, we can draw the image
    c.drawImage(image_path, x, y, width=img_width, height=img_height)
    c.save()
    print(f"[+] Watermark PDF created at {output_pdf_path}")


def create_watermark_from_text(text: str):
    """Creates a watermark from the given text"""
    if text:
        # Create a canvas
        c = canvas.Canvas('watermark.pdf', pagesize=letter)
        # Set the fill color to light grey
        c.setFillColorRGB(0.5, 0.5, 0.5)
        # Set the transparency
        c.setFillAlpha(0.5)
        # Set the font size and type
        c.setFont("Helvetica", 60)
        # Rotate according to the configured parameter
        # c.rotate(45)
        # Set the position of the watermark text
        c.drawCentredString(letter[0] / 2, letter[1] / 2, text)
        # Save the PDF
        c.save()
        print("[+] Watermark PDF created at watermark.pdf")
        


def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path):
    input_pdf = PdfReader(input_pdf_path)
    watermark_pdf = PdfReader(watermark_pdf_path)
    watermark_page = watermark_pdf.pages[0]
    # Create a PdfWriter object for the output PDF
    pdf_writer = PdfWriter()
    # Loop through all the pages and add them
    for page in input_pdf.pages:
        watermark_page_copy = deepcopy(watermark_page)
        # Merge the watermark with the page
        watermark_page_copy.merge_page(page)
        # Add the page from PdfReader to the output file
        pdf_writer.add_page(watermark_page_copy)
    # Write the output PDF
    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)
    # print success message
    print(f"[+] Watermark added to PDF at {output_pdf_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add watermark to pdf')
    parser.add_argument('input_pdf', help='input pdf file')
    parser.add_argument('output_pdf', help='output pdf file')
    parser.add_argument('-p', '--watermark_pdf', help='watermark pdf file')
    parser.add_argument('-i', '--watermark_image', help='watermark PNG image file')
    parser.add_argument('-t', '--watermark_text', help='watermark text')
    # parse the arguments
    args = parser.parse_args()
    if args.watermark_pdf:
        # directly add watermark pdf to input pdf
        add_watermark(args.input_pdf, args.output_pdf, args.watermark_pdf)
    elif args.watermark_image:
        # remove transparency from watermark image
        new_output_file = args.watermark_image.replace('.png', '_white.png')
        remove_transparency(args.watermark_image, new_output_file)
        # create watermark pdf from image
        create_watermark_from_image(new_output_file)
        # add watermark pdf to input pdf
        add_watermark(args.input_pdf, args.output_pdf, new_output_file.replace('.png', '.pdf'))
    elif args.watermark_text:
        # create watermark pdf from text
        create_watermark_from_text(args.watermark_text)
        # add watermark pdf to input pdf
        add_watermark(args.input_pdf, args.output_pdf, 'watermark.pdf')

