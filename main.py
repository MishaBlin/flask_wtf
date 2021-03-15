from flask import Flask, render_template, url_for

app = Flask(__name__)

prof_list = ['engineer', 'pilot', 'builder', 'doctor', 'biologist']


@app.route('/')
@app.route('/index/<title>')
def index(title='Mars'):
    return render_template('base.html', title=title)


@app.route('/list_prof/<kind>')
def profession(kind):
    return render_template('prof_list.html', type=kind, prof_list=prof_list)


data = {
    'title': 'Анкета',
    'surname': ('Фамилия', 'Рэмби'),
    'name': ('Имя', 'Джим'),
    'education': ('Образование', 'выше среднего'),
    'profession': ('Профессия', 'врач'),
    'motivation': ('Мотивация', 'желаю посетить космос'),
    'sex': ('Пол', 'male'),
    'ready': ('Готовы ли остаться на Марсе?', 'True')
}


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html', style_href=url_for('static', filename='css/style.css'), data_dict=data, title=data['title'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
