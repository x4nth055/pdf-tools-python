Before running the code, run:
```bash
$ pip install -r requirements.txt
```

Then, make sure to get an Apryse API key [here](https://dev.apryse.com/get-key). Then, put it in the `API_KEY` variable in the `pdf_compressor.py` script.

Finally, run the script with the PDF file you want to compress as an argument:
```bash
$ python pdf_compressor.py bert-paper.pdf

PDFNet is running in demo mode.
Permission: read
Permission: optimizer
Permission: write
Input file & size: bert-paper.pdf, 757.00KB
Output file & size: bert-paper_compressed.pdf, 497.04KB
Saved 34.34% space
```