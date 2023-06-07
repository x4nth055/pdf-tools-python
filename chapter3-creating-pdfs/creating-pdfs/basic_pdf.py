from reportlab.pdfgen import canvas

def create_pdf(output_filename):
    # Create a canvas
    c = canvas.Canvas(output_filename)
    # draw a string 100 points to the right and 750 points up from the bottom
    c.drawString(100, 750, "Hello World!")
    # save the PDF
    c.save()
    
create_pdf("basic.pdf")