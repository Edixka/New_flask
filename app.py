from flask import Flask, render_template

app = Flask(__name__)


# menu = [{"name": "Утечка фреона", "url": "Freon leak"},
#         {"name": "Засор капилярки", "url": "Capillary blockage"},
#         {"name": "Поломка компрессора", "url": "Compressor failure"},
#         {"name": "Доверте свою технику профиссионалу", "url": "Professional"}]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cont')
def cont():
    return render_template('cont.html')


@app.route('/capillary')
def capillary():
    return render_template('capillary.html')


if __name__ == '__main__':
    app.run(debug=True)
