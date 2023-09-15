import fitz  # PyMuPDF
import sys

# get the file path from the command line
input_pdf_path = sys.argv[1]
# get the pages to delete from the command line
pages_to_delete = [int(p) for p in sys.argv[2:]] # page numbering starts from 0
# Open the PDF file
pdf = fitz.open(input_pdf_path)

# Delete the pages
for page_num in sorted(pages_to_delete, reverse=True):
    pdf.delete_page(page_num)

# Save the modified PDF
output_pdf_path = f"{input_pdf_path[:-4]}_modified.pdf"
pdf.save(output_pdf_path)

# Close the PDF file
pdf.close()

print(f"Modified PDF saved as {output_pdf_path}.")
