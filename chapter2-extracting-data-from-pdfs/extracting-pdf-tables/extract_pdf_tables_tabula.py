import tabula
import os
import sys

# read the PDF file
pdf_filename = sys.argv[1]
tables = tabula.read_pdf(pdf_filename, pages='all')

# print the number of tables found
print("Total tables extracted:", len(tables))

# print the first table
print(tables[0])

table_filename = os.path.splitext(pdf_filename)[0] + "_table"
# iterate through all tables
for i, table in enumerate(tables):
    # export individually as CSV
    table.to_csv(table_filename + f"_{i+1}.csv")
    # export individually as Excel
    table.to_excel(table_filename + f"_{i+1}.xlsx")
    

# convert all tables of a PDF file into a single CSV file
# supported output_format: CSV, TSV, JSON
tabula.convert_into(pdf_filename, "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory into CSV files
tabula.convert_into_by_batch("pdfs", output_format='csv', pages='all')