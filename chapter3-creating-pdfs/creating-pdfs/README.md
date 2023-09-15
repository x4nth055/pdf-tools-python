To get started, install ReportLab:
```bash
$ pip install -r requirements.txt
```
Below are the scripts in this directory:
- [basic_pdf.py](basic_pdf.py): Create a basic PDF file with text and save it.
- [text_with_styles.py](text_with_styles.py): Create a PDF file with text and styles.
- [titles_and_paragraphs.py](titles_and_paragraphs.py): Create a PDF file with titles and paragraphs.
- [adding_bullet_points1.py](adding_bullet_points1.py): Create a PDF file with bullet points using HTML.
- [adding_bullet_points2.py](adding_bullet_points2.py): Create a PDF file with bullet points using `ListFlowable` and `ListItem`.
- [adding_tables.py](adding_tables.py): Create a PDF file with a table using `Table`.
- [adding_styled_tables.py](adding_styled_tables.py): Create a PDF file with a table using `Table` and styles.
- [adding_images.py](adding_images.py): Create a PDF file with an image using `Image`.
- [adding_charts.py](adding_charts.py): Create a PDF file with a chart using `Drawing`.
- [adding_pagination_header_footer.py](adding_pagination.py): Create a PDF file with pagination, headers, and footers using `SimpleDocTemplate`.
- [generating-invoices/invoice_generator.py](generating-invoices/invoice_generator.py): Create a PDF file with an invoice from a CSV file using `SimpleDocTemplate`.