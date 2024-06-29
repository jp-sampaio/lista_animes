from flask import Flask, render_template, request, redirect, url_for
from models import db, Anime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Garantir que as tabelas sejam criadas antes do primeiro acesso
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    animes = Anime.query.all()
    return render_template('index.html', animes=animes)

@app.route('/add', methods=['POST'])
def add_anime():
    title = request.form.get('title')
    genre = request.form.get('genre')
    new_anime = Anime(title=title, genre=genre)
    db.session.add(new_anime)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_anime(id):
    anime = Anime.query.get(id)
    db.session.delete(anime)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)