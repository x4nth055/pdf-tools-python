To get started:
```bash	
$ pip install PyMuPDF
```
To hide (redact) all instances of the word "python" in `Chapter_2_Building_Malware.pdf` in red:

```bash
$ python highlight_text.py Chapter_2_Building_Malware.pdf -k python -s redaction -c 1 0 0 
```

To highlight all instances of the words "python" and "pdf" in `Chapter_2_Building_Malware.pdf` in green:

```bash
$ python highlight_text.py Chapter_2_Building_Malware.pdf -k python pdf -s highlight -c 0 1 0
```