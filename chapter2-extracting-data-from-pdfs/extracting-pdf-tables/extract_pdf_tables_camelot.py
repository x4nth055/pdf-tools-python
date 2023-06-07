import camelot
import sys
import os

# Get the PDF filename from the command line
file = sys.argv[1]

# Read the PDF file
tables = camelot.read_pdf(file)

# Print the number of tables found
print("Total tables extracted:", tables.n)

# Print the first table
print(tables[0].df)

table_filename = os.path.splitext(file)[0] + "_table"
# export individually as CSV
tables[0].to_csv(table_filename + "_1.csv")
# export individually as Excel
tables[0].to_excel(table_filename + "_1.xlsx")

# or export all in a zip
tables.export(table_filename + "_all.zip", f="csv")

# export to HTML
tables.export(table_filename + "_all.html", f="html")
