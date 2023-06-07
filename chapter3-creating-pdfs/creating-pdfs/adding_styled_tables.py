# adding_styled_tables.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def create_pdf_with_styled_table(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    title = Paragraph("My Document Title", styles['Title'])
    flowables.append(title)

    flowables.append(Spacer(1, 12))

    table_data = [
        ['Name', 'Age', 'City'],
        ['Abdou', '24', 'Constantine'],
        ['Bob', '28', 'Los Angeles'],
        ['Charlie', '30', 'Zurich']
    ]

    # Create a TableStyle and add it to the table
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # add grey background to header row
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # set header row text color to white

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # align all text to center
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # set header row font to bold
        ('FONTSIZE', (0, 0), (-1, 0), 14),  # set header row font size

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # add extra padding to the header row
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # set background color of data rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # add grid lines
    ])

    table = Table(table_data, style=table_style)
    flowables.append(table)

    doc.build(flowables)

create_pdf_with_styled_table("my_document_with_styled_table.pdf")
