from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", template_folder='templates')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    txt = translator.english_to_french(textToTranslate)
    return txt

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    txt = translator.french_to_english(textToTranslate)
    return txt

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
