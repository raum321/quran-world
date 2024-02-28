from flask import Flask, render_template
from dependencies import parse_quran, return_suras, font_map

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<rewayah>')
def quran(rewayah):
    quran = parse_quran(rewayah)
    suras = return_suras(quran)

    return render_template('quran.html', quran=quran, suras= suras, rewayah=rewayah, font=font_map[rewayah])

if __name__ == '__main__':
    app.run(debug=True)
