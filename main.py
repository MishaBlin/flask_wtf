from flask import Flask, render_template

app = Flask(__name__)

prof_list = ['engineer', 'pilot', 'builder', 'doctor', 'biologist']


@app.route('/')
@app.route('/index/<title>')
def index(title='Mars'):
    return render_template('base.html', title=title)


@app.route('/list_prof/<kind>')
def profession(kind):
    return render_template('prof_list.html', type=kind, prof_list=prof_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
