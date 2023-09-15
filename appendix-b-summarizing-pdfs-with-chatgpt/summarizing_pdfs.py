import openai
import fitz
import sys

# Put your OpenAI key here
openai.api_key = "YOUR_API_KEY"
# default model to use
default_model = "gpt-3.5-turbo"
# the maximum number of characters the model can process
model_character_limit = {
    "gpt-3.5-turbo": int(4_000 * 2.2),
    "gpt-4": int(8_000 * 2.2),
    "gpt-3.5-turbo-16k": int(16_000 * 2.2),
    "gpt-4-32k": int(32_000 * 2.2),
}

def get_pdf_content(pdf_path):
    """Extracts text from a PDF file and returns it as a string"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += "\n" + page.get_text()
    return text


def get_summary(pdf_content, model):
    max_characters = model_character_limit.get(model, model_character_limit[default_model])
    if len(pdf_content) > max_characters:
        print(f"PDF content length ({len(pdf_content)}) exceeds the maximum number of characters ({max_characters}). Truncating text to {max_characters} characters.")
    while True:
        try:
            completion = openai.ChatCompletion.create(**{
                "model": model,
                "messages": [
                    {"role": "system", "content": "You're an expert PDF document summarizer. Given a PDF document, you summarize it and output Markdown text."},
                    {"role": "user", "content": pdf_content[:max_characters]},
                ],
                "temperature": 0.05,
            })
            return completion.choices[0].message.content.strip()
        except openai.error.InvalidRequestError as e:
            if e.code == "context_length_exceeded":
                max_characters -= 100  # Reduce by 100 characters
                print(f"Context length exceeded. Truncating text to {max_characters} characters and trying again.")
                if max_characters <= 0:
                    raise ValueError("Text is too short to be summarized.")
            else:
                raise  # Raise the original exception if it's not a context_length_exceeded error


if __name__ == "__main__":
    # path to the PDF file
    pdf_path = sys.argv[1]
    # output file in Markdown format
    output_file = sys.argv[2]
    # model to use
    try:
        model = sys.argv[3]
    except IndexError:
        model = default_model
    pdf_content = get_pdf_content(pdf_path)
    print(f"PDF content length (in characters): {len(pdf_content)}")
    print("=" * 80)
    summary = get_summary(pdf_content, model)
    print(f"Summary: {summary}")
    with open(output_file, "w") as f:
        f.write(summary)