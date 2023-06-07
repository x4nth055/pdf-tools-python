# adding_bullet_points2.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_with_bullet_list(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    title = Paragraph("My Document Title", styles['Title'])
    flowables.append(title)
    
    flowables.append(Spacer(1, 12))

    bullet_list = ListFlowable(
        [
            ListItem(Paragraph("Item 1", styles["BodyText"])),
            ListItem(Paragraph("Item 2", styles["BodyText"])),
            ListItem(Paragraph("Item 3", styles["BodyText"])),
        ],
        bulletType='bullet',
        start='circle',  # or use 'disc' or 'square' for different bullet shapes
    )
    # bullet_list = ListFlowable(
    #     [
    #         ListItem(Paragraph("Item 1", styles["BodyText"]), bulletChr=u'\u2023'),
    #         ListItem(Paragraph("Item 2", styles["BodyText"]), bulletChr=u'\u2023'),
    #         ListItem(Paragraph("Item 3", styles["BodyText"]), bulletChr=u'\u2023'),
    #     ],
    #     bulletType='bullet',
    # )

    flowables.append(bullet_list)
    another_bullet_list = ListFlowable(
        [
            ListItem(Paragraph("Item 1", styles["BodyText"])),
            ListItem(Paragraph("Item 2", styles["BodyText"])),
            ListItem(Paragraph("Item 3", styles["BodyText"])),
            ListItem(Paragraph("Item 4", styles["BodyText"])),
            ListItem(Paragraph("Item 5", styles["BodyText"])),
            ListItem(Paragraph("Item 6", styles["BodyText"])),
        ],
        bulletType='I',
        start=1,  # or use 'a' or 'A' for different numberings
    )
    flowables.append(another_bullet_list)
    doc.build(flowables)


create_pdf_with_bullet_list("my_document_with_bullet_list.pdf")
