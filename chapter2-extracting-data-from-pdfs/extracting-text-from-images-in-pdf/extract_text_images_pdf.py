import fitz
import io
import pytesseract
from PIL import Image

def pdf_image_to_text(pdf_path):
    # Open the pdf
    doc = fitz.open(pdf_path)
    text_output = ""
    for page in doc:
        # Iterate through images on the page
        for img in page.get_images():
            xref = img[0]
            # Extract image bytes
            base = doc.extract_image(xref)
            image_data = base["image"]
            # Convert to PIL image
            image = Image.open(io.BytesIO(image_data))
            # Use tesseract to convert to text
            text = pytesseract.image_to_string(image)
            # Add to text output with a new line
            text_output += text + "\n"
    return text_output


if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1]
    # Extract text from images in pdf
    text = pdf_image_to_text(pdf_path)
    # Print text
    print(text)