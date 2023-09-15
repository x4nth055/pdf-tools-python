import fitz  # PyMuPDF
import argparse

def find_keywords_in_pdf(pdf_path, keywords, highlight_style="highlight", color=(0, 1, 0)):
    # Open the PDF file
    pdf = fitz.open(pdf_path)
    # iterate over pages
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        # Apply redactions flag
        apply_redactions_flag = False
        # Search each keyword on the page
        for keyword in keywords:
            search_instances = page.search_for(keyword)
            # Apply the selected highlight style
            for instance in search_instances:
                if highlight_style == "highlight":
                    annot = page.add_highlight_annot(instance)
                elif highlight_style == "underline":
                    annot = page.add_underline_annot(instance)
                elif highlight_style == "redaction":
                    annot = page.add_redact_annot(instance)
                    annot.set_info(title="Redact")
                    apply_redactions_flag = True
                # Apply color
                if highlight_style == "redaction":
                    annot.set_colors({"stroke": color, "fill": color})
                else:
                    annot.set_colors(stroke=color)
                # Update the annotation
                annot.update()
        # Apply redactions for the current page if needed
        if apply_redactions_flag:
            page.apply_redactions()
    # Save the PDF file
    pdf.save(highlight_style + "_" + pdf_path)
    # Close the PDF file
    pdf.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highlight keywords in a PDF.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("-k", "--keywords", required=True, nargs='+', help="Keywords to search for in the PDF")
    parser.add_argument("-s", "--style", choices=["highlight", "underline", "redaction"], default="highlight", help="Style of highlight")
    parser.add_argument("-c", "--color", nargs=3, type=float, default=[0, 1, 0], help="Color for highlighting (three floats between 0 and 1)")
    # Parse the arguments
    args = parser.parse_args()
    # Highlight the keywords in the PDF
    find_keywords_in_pdf(args.pdf_path, args.keywords, args.style, tuple(args.color))
