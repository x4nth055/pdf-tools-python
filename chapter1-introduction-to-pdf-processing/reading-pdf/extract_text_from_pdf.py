import fitz
import argparse
import os

# wrap the above in a function
def extract_text(pdf_file, output_file, by_page=False, output_folder="results"):
    """Extract the text from a PDF file and save it to a text file.
    If by_page is True, each page is saved to a separate text file.
    Args:
        pdf_file (str): Path to the PDF file to be extracted.
        output_file (str): Path to the output file.
        by_page (bool, optional): If True, save each page to a separate text file.
            Defaults to False."""
    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # open the pdf
    doc = fitz.open(pdf_file)
    # get the number of pages
    num_pages = doc.page_count
    # if by_page is True, save each page to a separate text file
    if by_page:
        # get the name of the output file
        file_name = os.path.basename(output_file)
        # get the name of the output file without the extension
        file_name = os.path.splitext(file_name)[0]
        # iterate over the pages
        for i in range(num_pages):
            # load the page
            page = doc.load_page(i)
            # get the text
            page_text = page.get_text()
            # create a text file
            with open(os.path.join(output_folder, f"{file_name}_page_{i+1}.txt"), "w") as f:
                # write the text to the file
                f.write(page_text)
    else:
        # get the text of all the pages
        for i in range(num_pages):
            # load the page
            page = doc.load_page(i)
            # get the text
            page_text = page.get_text()
            # create a text file
            with open(os.path.join(output_folder, output_file), "a") as f:
                # add a header to separate the pages
                f.write(f"--- Page {i+1} ---\n")
                # write the text to the file
                f.write(page_text)

                
if __name__ == "__main__":
    # create the parser object
    parser = argparse.ArgumentParser(description="Extract the text from a PDF file.")
    # add the arguments
    parser.add_argument("pdf_file", help="Path to the PDF file to be extracted.")
    parser.add_argument("output_file", help="Path to the output file.")
    parser.add_argument("--output_folder", help="Path to the output folder.", default="results")
    parser.add_argument(
        "--by_page",
        help="If True, save each page to a separate text file.",
        action="store_true",
    )
    # parse the arguments
    args = parser.parse_args()
    # extract the text
    extract_text(args.pdf_file, args.output_file, args.by_page)
