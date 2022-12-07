from machinetranslation import translator
from flask import Flask, render_template, request
import json
import translator as tr

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    test_to_translate = request.args.get('text_to_translate')
    var frenc_text = tr.english_to_french(text_to_translate)
    return "Translated text to French"

@app.route("/french_to_english")
def french_to_english():
    text_to_translate = request.args.get('text_to_translate')
    var english_text = tr.french_to_english(text_to_translate)
    return english_text

@app.route("/")
def render_index_page():
    render_template('index.html')

if __name__ == "__main__":
    render_index_page()
    app.run(host="0.0.0.0", port=8080)

