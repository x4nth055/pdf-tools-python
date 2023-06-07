# adding_images.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_with_image(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    title = Paragraph("My Document Title", styles['Title'])
    flowables.append(title)

    flowables.append(Spacer(1, 12))

    # Create an Image object from an image file and add it to the list of flowables
    img = Image('python_logo.png', width=200, height=200)
    flowables.append(img)

    doc.build(flowables)

create_pdf_with_image("my_document_with_image.pdf")
