# adding_tables.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_with_table(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    title = Paragraph("My Document Title", styles['Title'])
    flowables.append(title)

    flowables.append(Spacer(1, 12))

    # Define a 2D list with data for the table
    table_data = [
        ['Name', 'Age', 'City'],
        ['Abdou', '24', 'Constantine'],
        ['Bob', '28', 'Los Angeles'],
        ['Charlie', '30', 'Zurich']
    ]

    # Create a Table object and add it to the list of flowables
    table = Table(table_data)
    flowables.append(table)

    doc.build(flowables)

create_pdf_with_table("my_document_with_table.pdf")
