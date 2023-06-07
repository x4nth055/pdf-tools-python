To get started, install the dependencies:
```bash
$ pip install -r requirements.txt
```
- Using Camelot:
  ```bash
  $ python extract_pdf_tables_camelot.py pdfs/foo.pdf
  ```
  Or:
  ```bash
  $ python extract_pdf_tables_camelot_argparse.py pdfs/foo.pdf --extension html
  ```
- Using Tabula:
  ```bash
  $ python extract_pdf_tables_tabula.py pdfs/1710.05006.pdf
  ```
  Or:
  ```bash
  $ python extract_pdf_tables_tabula_argparse.py --input pdfs/1710.05006.pdf --extension json
  ```
- Using PDFPlumber:
  ```bash
  $ python extract_pdf_tables_pdfplumber.py pdfs/1710.05006.pdf

    Method\n/Rank    AVG Net-\nwork Neg.\nNet-\nwork Streaks Milia-\nLike\nCyst
  0        [22]/1  0.895      0.945            0.869   0.960              0.807
  1        [23]/2  0.833      0.835            0.762   0.896              0.838
  2        [23]/3  0.832      0.828            0.762   0.900              0.837
        Method AVG-\nAUC M-\nAUC SK-\nAUC M-\nSP82 M-\nSP89 M-\nSP95 M-\nSENS M-\nSPEC SK-\nSENS SK-\nSPEC
  0  [24]TopAVG     0.911   0.868    0.953    0.729    0.588    0.366    0.735    0.851     0.978     0.773
  1   [25]TopSK     0.910   0.856    0.965    0.727    0.555    0.404    0.103    0.998     0.178     0.998
  2    [26]TopM     0.908   0.874    0.943    0.747    0.590    0.395    0.547    0.950     0.356     0.990
  3       AVGSC     0.913   0.872    0.954    0.778    0.605    0.435    0.214    0.988     0.600     0.975
  4       L-SVM     0.926   0.892    0.960    0.834    0.692    0.571    0.718    0.901     0.878     0.931
  5      NL-SVM     0.904   0.853    0.955    0.801    0.449    0.168    0.675    0.909     0.889     0.928
  ```