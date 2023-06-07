import fitz
from pprint import pprint
from utils import transform_date
import sys

# target file
pdf_filename = sys.argv[1]
# load the PDF
doc = fitz.open(pdf_filename)
# get the metadata
pdf_metadata = doc.metadata
# turn the dates into python datetime objects
if "creationDate" in pdf_metadata:
    pdf_metadata["creationDate"] = transform_date(pdf_metadata["creationDate"])
if "modDate" in pdf_metadata:
    pdf_metadata["modDate"] = transform_date(pdf_metadata["modDate"])
    
pprint(pdf_metadata)
