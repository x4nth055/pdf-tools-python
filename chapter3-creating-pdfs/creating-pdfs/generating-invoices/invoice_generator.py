import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Create a PDF document
pdf = SimpleDocTemplate(
    "professional_invoice.pdf", pagesize=letter
)

# Read data from CSV
data = []
with open('invoice_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

# Table style with more customization
# style = TableStyle([
#     ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
#     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#     ('FONTSIZE', (0, 0), (-1, 0), 14),
#     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#     ('GRID', (0, 0), (-1, -1), 1, colors.black)
# ])
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])


# Create table
table = Table(data)
table.setStyle(style)

# Add table to elements to build
elements = []
styles = getSampleStyleSheet()
custom_style = ParagraphStyle(
    name='CustomTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=24,
    textColor=colors.blue,
    alignment=1,
)
title = Paragraph("Professional Invoice", custom_style)
elements.append(title)
elements.append(Spacer(1, 0.5 * inch))
elements.append(table)

# Generate PDF
pdf.build(elements)
