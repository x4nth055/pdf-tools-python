import fitz

doc = fitz.open('Chapter_2_Building_Malware.pdf')
page = doc[0]

# Create a matrix that scales the image to half its original size
matrix = fitz.Matrix(0.5, 0.5)

# Define the portion of the page to render (upper left quarter)
clip = fitz.Rect(0, 0, page.rect.width / 2, page.rect.height / 2)

# Get the pixmap with the specified parameters
pixmap = page.get_pixmap(matrix=matrix, colorspace='gray', clip=clip, alpha=True)

# Save the pixmap as an image
pixmap.save('output.png')
