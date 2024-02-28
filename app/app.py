from flask import Flask, render_template
from parse import parse_quran
from font_map import font_map

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<rewayah>')
def quran(rewayah):
    quran = parse_quran(rewayah)

    return render_template('quran.html', quran=quran, rewayah=rewayah, font=font_map[rewayah])

if __name__ == '__main__':
    app.run(debug=True)
