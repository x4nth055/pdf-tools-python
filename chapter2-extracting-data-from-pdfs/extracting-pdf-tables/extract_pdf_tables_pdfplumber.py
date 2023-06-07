import pdfplumber
import pandas as pd
import sys

# read the PDF file name from the command line
pdf_filename = sys.argv[1]
# open the PDF file
with pdfplumber.open(pdf_filename) as pdf:
    # iterate through the pages
    for i in range(len(pdf.pages)):
        # extract the page as a table
        table = pdf.pages[i].extract_table()
        if table is None:
            # skip the page if it does not contain any tables
            continue
        # convert it into a Pandas dataframe
        df = pd.DataFrame(table[1:], columns=table[0])
        # print the dataframe
        print(df)
        # export individually as CSV
        df.to_csv(f"table_{i+1}.csv")
        # export individually as Excel
        df.to_excel(f"table_{i+1}.xlsx")