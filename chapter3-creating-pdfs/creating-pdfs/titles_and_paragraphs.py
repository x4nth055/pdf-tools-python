from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(output_filename):
    # Create a SimpleDocTemplate object with a specified pagesize (letter)
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    # Get a sample style sheet from ReportLab
    styles = getSampleStyleSheet()
    # Prepare an empty list to hold flowable objects
    flowables = []
    # Create a title Paragraph using the 'Title' style from the stylesheet
    # Add this Paragraph to the list of flowables
    title = Paragraph("My Document Title", styles['Title'])
    flowables.append(title)
    # Add a Spacer to the list of flowables. This will provide a vertical
    # space of 12 points between the title and the subsequent content
    flowables.append(Spacer(1, 12))
    # Create a text for the body of the document
    # HTML tags can be used to provide inline styling
    text = """
    This is a paragraph in my document. It has multiple sentences
    and can contain <b>bold</b> or <i>italic</i> text.
    <br></br><br></br>
    This should be a new paragraph, with two newlines after the
    first line. This is a <a href="https://thepythoncode.com">link</a> to thepythoncode.com.
    However, unlike HTML on the browser, it is not styled as a link, 
    as you need to manually style it here as a styled one: <font color="blue"><u><a href="https://thepythoncode.com">link</a></u></font>.
    """
    # Create a Paragraph using the 'BodyText' style from the stylesheet
    # Add this Paragraph to the list of flowables
    paragraph = Paragraph(text, styles['BodyText'])
    flowables.append(paragraph)
    # Build the document using the list of flowables that we have created
    # The order of the flowables in the list will determine their order in the document
    doc.build(flowables)

create_pdf("titles_and_paragraphs.pdf")
