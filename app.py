from flask import Flask, render_template, request
from newspaper_extraction import extract_article_text
from translator import translate_text
from summarization import summarize_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def summarize():
    input_type = request.form.get("input_type")
    target_language = request.form.get("language")
    content=None
    if input_type == "url":
        url = request.form.get("url")
        content = extract_article_text(url)
    elif input_type == "text":
        content = request.form.get("text")
    
    if content is not None:  # Check if content is assigned a value
        summary = summarize_text(content)
        print("Summary:", summary)  # Debugging print statement
        if summary:  # Check if summary is not empty
            translated_summary = translate_text(summary, target_lang=target_language)
            return render_template('result.html', summary=translated_summary)
        else:
            return "Failed to summarize the text."
    else:
        return "Invalid input type."


if __name__ == '__main__':
    app.run(debug=True)
