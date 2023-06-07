Install the requirements:
```bash
$ pip install -r requirements.txt
```
Then, run the script:
```bash
$ python extract_pdf_links.py Chapter_2_Building_Malware.pdf
Page 2: https://en.wikipedia.org/wiki/Scrypt
Page 2: https://docs.python.org/3/library/secrets.html
...<SNIPPED>...
Page 12: https://www.thepythoncode.com/article/use-gmail-api-in-python
Page 12: https://www.thepythoncode.com/article/use-gmail-api-in-python
Page 15: https://www.thepythoncode.com/article/sending-emails-in-python-smtplib
...<SNIPPED>...
Page 52: https://www.thepythoncode.com/article/get-hardware-system-information-python
Page 60: https://en.wikipedia.org/wiki/Secure_copy_protocol
```
A new file will be created, `Chapter_2_Building_Malware_links.txt` that contains all the links extracted from the PDF file.