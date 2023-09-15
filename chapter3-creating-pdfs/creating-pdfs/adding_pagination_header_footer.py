from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak

# Initialize the PDF
pdf = SimpleDocTemplate("example_pagination.pdf", pagesize=letter)
styles = getSampleStyleSheet()
content = []

# Add dummy content to make it a 10-page PDF
for i in range(1, 11):
    para = Paragraph(f"This is paragraph {i} on page {i}.", styles['Normal'])
    content.append(para)
    content.append(PageBreak())  # Add a page break after each paragraph

# Custom function to add page numbers, headers, and footers
def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    # add page number
    canvas.drawRightString(200 * mm, 20 * mm, f"Page {page_num}")
    # add header and footer
    canvas.drawString(20 * mm, 260 * mm, "My Header")
    canvas.drawString(20 * mm, 20 * mm, "My Footer")
    
    
# Build the PDF
pdf.build(content, onFirstPage=add_page_number, onLaterPages=add_page_number)

print("The PDF example_pagination.pdf with pagination, headers, and footers has been generated.")
