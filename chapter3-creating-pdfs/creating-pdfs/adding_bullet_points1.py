# adding_bullet_points1.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_with_bullets(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    title = Paragraph("My Document Title", styles['Title'])
    flowables.append(title)

    flowables.append(Spacer(1, 12))

    # Create bullet points
    bullet_points = [
        '<bullet>\u2022</bullet>Abdou is 24 years old and lives in Constantine.',
        '<bullet>\u2022</bullet>Bob is 28 years old and lives in Los Angeles.',
        '<bullet>\u2022</bullet>Charlie is 30 years old and lives in Zurich.'
    ]
    for point in bullet_points:
        p = Paragraph(point, styles['BodyText'])
        flowables.append(p)

    doc.build(flowables)

create_pdf_with_bullets("my_document_with_bullets.pdf")
