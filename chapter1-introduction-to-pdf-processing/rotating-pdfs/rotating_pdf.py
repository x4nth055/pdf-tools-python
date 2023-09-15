import fitz  # PyMuPDF
import sys

# get the path to the PDF file
input_pdf_path = sys.argv[1]
# rotation angle is in degrees, clockwise
# 0 degrees is the default rotation angle
# 90 degrees will rotate the page 90 degrees, clockwise
# 180 degrees will rotate the page 180 degrees, clockwise, same as -180 degrees, counter-clockwise
# 270 degrees will rotate the page 270 degrees, clockwise, same as -90 degrees, counter-clockwise
# -90 degrees will rotate the page 90 degrees, counter-clockwise
# -270 degrees will rotate the page 270 degrees, counter-clockwise, same as 90 degrees, clockwise
rotation_degrees = int(sys.argv[2])
# Open the PDF file
pdf = fitz.open(input_pdf_path)
# Loop through each page
for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)
    # Get the existing rotation angle
    current_rotation = page.rotation
    print(f"Page {page_num} has a rotation angle of {current_rotation} degrees.")
    # adding 180 degrees to the current rotation angle will rotate the page 180 degrees, clockwise
    # another example: subtracting 90 degrees from the current rotation angle will rotate the page 90 degrees, counter-clockwise
    # Calculate the new rotation angle
    new_rotation = (current_rotation + rotation_degrees) % 360
    # Set the new rotation angle
    page.set_rotation(new_rotation)
    print(f"Page {page_num} has a new rotation angle of {page.rotation} degrees.")

# Save the rotated PDF
output_pdf_path = f"{input_pdf_path[:-4]}_rotated{rotation_degrees}.pdf"
pdf.save(output_pdf_path)
# Close the PDF file
pdf.close()

print(f"Rotated PDF saved as {output_pdf_path}.")
