import argparse
import fitz
import os

def pdf_to_image(pdf_file, output_folder, matrix, pages, clip, colorspace, alpha):
    # Load the PDF
    doc = fitz.open(pdf_file)
    # Parse the page numbers
    if pages == 'all':
        page_numbers = range(len(doc))
    else:
        page_numbers = [int(page) for page in pages.split(',')]
    # Loop through the pages
    for page_number in page_numbers:
        # Get the page
        page = doc[page_number]
        # Parse the clip
        if clip:
            clip_values = [float(value) for value in clip.split(',')]
            clip_rect = fitz.Rect(*clip_values)
        else:
            clip_rect = None
        # Get the pixmap
        pixmap = page.get_pixmap(
            matrix=fitz.Matrix(*matrix),
            colorspace=colorspace,
            clip=clip_rect,
            alpha=alpha,
        )
        # Make the output filename
        output_filename = f"{pdf_file[:-4]}_{page_number+1}.png"
        # the full path to the output file
        image_filename = os.path.join(output_folder, output_filename)
        # Save the pixmap as an image
        pixmap.save(image_filename)
        print(f"Image saved as {image_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PDF pages to images.')
    parser.add_argument('pdf_file', help='The PDF file to convert.')
    parser.add_argument("-o", "--output-folder", default="output", help="The folder to save the output images in.")
    parser.add_argument('-m', '--matrix', default=(1.0, 1.0), nargs=2, type=float, help='The scale factors in the x and y directions.')
    parser.add_argument('-p', '--pages', default='all', help='The page numbers to convert, separated by commas.')
    parser.add_argument('-c', '--clip', default=None, help='The clip rectangle, as a comma-separated list of four numbers: x0, y0, x1, y1.')
    parser.add_argument('-cs', '--colorspace', default='rgb', choices=['rgb', 'gray', 'rgba', 'cmyk'], help='The color space of the output images.')
    parser.add_argument('-a', '--alpha', action='store_true', help='Include an alpha channel in the output images.')
    # Parse the arguments
    args = parser.parse_args()
    # Make the output folder if it doesn't exist
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    # Convert the PDF to images
    pdf_to_image(args.pdf_file, args.output_folder, args.matrix, args.pages, args.clip, args.colorspace, args.alpha)
