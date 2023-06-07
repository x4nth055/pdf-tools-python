from reportlab.pdfgen import canvas

def create_pdf(output_filename):
    c = canvas.Canvas(output_filename)
    # set the font of the document to Helvetica, size 14
    c.setFont("Helvetica", 14)
    # draw a string 100 points to the right and 750 points up from the bottom
    c.drawString(100, 750, "Hello, World!")
    # set Times-Roman as the font with a size of 12
    c.setFont("Times-Roman", 12)
    # draw a string 100 points to the right and 730 points up from the bottom
    c.drawString(100, 730, "This is another line.")
    # set the font to Helvetica-Bold, size 14
    c.setFont("Helvetica-Bold", 14)
    # draw a string 100 points to the right and 710 points up from the bottom
    c.drawString(100, 710, "This text is bold.")
    # set the font to Times-BoldItalic
    c.setFont("Times-BoldItalic", 14)
    # draw a string 100 points to the right and 690 points up from the bottom
    c.drawString(100, 690, "This text is bold and italic.")
    # save the PDF
    c.save()

create_pdf("basic-styling.pdf")
