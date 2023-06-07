Before running the script, install the required libraries:
```bash
$ pip install -r requirements.txt
```
Adding an image (`python_logo.png`) watermark to our `bert-paper.pdf` document, the output PDF is `output.pdf`:
```bash
$ python watermark_pdf.py bert-paper.pdf output.pdf -i python_logo.png
[+] Transparency removed from python_logo.png and saved at python_logo_white.png
[+] Watermark PDF created at python_logo_white.pdf
[+] Watermark added to PDF at output.pdf
```

Or directly from a PDF watermark file:
```bash
$ python watermark_pdf.py bert-paper.pdf output.pdf -p python_logo_white.pdf 
[+] Watermark added to PDF at output.pdf
```
Or a text watermark:
```bash
$ python watermark_pdf.py bert-paper.pdf output.pdf -t "thepythoncode.com"
[+] Watermark PDF created at watermark.pdf
[+] Watermark added to PDF at output.pdf
```