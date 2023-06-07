import fitz  # PyMuPDF

# Open the PDF
doc = fitz.open('Chapter_2_Building_Malware.pdf')

# Get the number of pages
print("Number of pages: ", doc.page_count)

# load the first page
first_page = doc.load_page(0)  # 0 represents the first page

# Get the text of the first page
first_page_text = first_page.get_text()
print(first_page_text)

# Get the text of all the pages
for i in range(doc.page_count):
    # load the page
    page = doc.load_page(i)
    # get the text
    page_text = page.get_text()
    # print the text
    print(f"--- Page {i+1} ---")
    print(page_text)
