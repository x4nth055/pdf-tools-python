import markdown2
import pdfkit
import sys

def markdown_to_pdf(markdown_file_path, pdf_file_path):
    # Read Markdown file
    with open(markdown_file_path, 'r') as f:
        markdown_text = f.read()

    # Convert to HTML
    html_text = markdown2.markdown(markdown_text)
    # Convert to PDF
    pdfkit.from_string(html_text, pdf_file_path)

if __name__ == '__main__':
    markdown_file_path = sys.argv[1]
    pdf_file_path = sys.argv[2]
    markdown_to_pdf(markdown_file_path, pdf_file_path)
