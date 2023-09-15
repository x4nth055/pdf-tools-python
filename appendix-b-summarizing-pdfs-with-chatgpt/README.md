To get started:
```bash
$ pip install pymupdf openai
```
To summarize a `bert-paper.pdf` file and save the summary to `bert-paper_summary.md`:
```bash
$ python summarizing_pdfs.py bert-paper.pdf bert-paper_summary.md
```
To change model to GPT-4:
```bash
$ python summarizing_pdfs.py bert-paper.pdf bert-paper_summary.md gpt-4
```