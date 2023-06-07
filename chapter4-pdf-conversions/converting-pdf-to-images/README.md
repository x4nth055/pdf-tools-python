To get started, install the required packages:

```bash
$ pip install -r requirements.txt
```

To convert a PDF to images, use the following command:

```bash
$ python convert_pdf_to_image.py Chapter_2_Building_Malware.pdf -o images -p 0,1,2,3,4 -m 2 2 -c 153,198,459,594 -cs gray -a
```
Or:
```bash
$ python convert_pdf_to_image.py Chapter_2_Building_Malware.pdf -o images -m 2 2
```