from dotenv import dotenv_values
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_pymongo import PyMongo
from forms import FormLogin
app = Flask(__name__)

config = dotenv_values(".env")

app.config['SENHA'] = config['PASSWORD']
app.config['SECRET_KEY'] = config['CHAVE']
app.config['MONGO_URI'] = config['MONGO_URI']
mongo = PyMongo(app)

# Área Home
todos_registros = mongo.db.MyCollection.find({})

top_pacotes = mongo.db.MyCollection.find(
    {'rating': {'$gte': 4.9}},
    {'_id': 0, 'image': 1, 'title': 1, 'rating': 1, 'description': 1, 'price': 1}
)


@app.route('/', methods=['GET', 'POST'])
def home():
    form_login = FormLogin()
    # Para Debugar
    # if request.method == 'POST':
    #     print(request.form)
    #     print(f"Usuário: {form_login.usuario.data}, Senha: {
    #           form_login.senha.data}")
    if form_login.validate_on_submit():
        if (form_login.usuario.data == 'admin' and form_login.senha.data == app.config.get('SENHA')):
            return redirect(url_for('login'))
        else:
            flash('Acesso Recusado! Revise as crendiciais!', 'erro')
            return redirect(url_for('home'))

    return render_template('home.html',
                           form_login=form_login,
                           registros=todos_registros,
                           top_pacotes=top_pacotes)

# Área de Admin


@app.route('/area-admin', methods=['GET', 'POST'])
def login():
    flash('Login realizado com Sucesso!', 'success')
    return render_template('area-admin.html', registros=todos_registros)
