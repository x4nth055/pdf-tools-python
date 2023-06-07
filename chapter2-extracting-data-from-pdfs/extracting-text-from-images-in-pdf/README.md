To get started:
```bash
$ pip install -r requirements.txt
```
You also have to install [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html).

Then, run the script on the target PDF:
```bash
$ python extract_text_images_pdf.py image.pdf
Abstract

We introduce a new language representa-
tion model called BERT, which stands for
Bidirectional Encoder Representations from
Transformers. Unlike recent language repre-
sentation models (Peters et al., 2018a; Rad-
ford et al., 2018), BERT is designed to pre-
train deep bidirectional representations from
unlabeled text by jointly conditioning on both
left and right context in all layers. As a re-
sult, the pre-trained BERT model can be fine-
tuned with just one additional output layer
to create state-of-the-art models for a wide
range of tasks, such as question answering and
language inference, without substantial task-
specific architecture modifications.

There are two existing strategies for apply-
ing pre-trained language representations to down-
stream tasks: feature-based and fine-tuning. The
feature-based approach, such as ELMo (Peters
et al., 2018a), uses task-specific architectures that
include the pre-trained representations as addi-
tional features. The fine-tuning approach, such as
the Generative Pre-trained Transformer (OpenAI
GPT) (Radford et al., 2018), introduces minimal
task-specific parameters, and is trained on the
downstream tasks by simply fine-tuning all pre-
trained parameters. The two approaches share the
same objective function during pre-training, where
they use unidirectional language models to learn
general language representations.
```