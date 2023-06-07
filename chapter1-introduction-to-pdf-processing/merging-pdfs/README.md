Install the required packages:
```bash
$ pip install -r requirements.txt
```
Then, run the script:
```bash
$ python pdf_merger.py python_cheat_sheet.pdf Chapter_2_Building_Malware.pdf
```
This will merge the two PDFs into a new PDF called `merged.pdf`. The first argument is the name of the script, the second argument is the name of the first PDF, and the third argument is the name of the second PDF. You can add as many PDFs as you want to merge, like so:
```bash
$ python pdf_merger.py file1.pdf file2.pdf file3.pdf file4.pdf
```