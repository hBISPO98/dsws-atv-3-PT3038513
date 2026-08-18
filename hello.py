# Importações de bibliotecas e ferramentas necessárias
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Inicialização de Flask e definição de chave secreta
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave Forte'

bootstrap = Bootstrap(app)

# Criação do formulário e suas definições
class NameForm(FlaskForm):
  name = StringField('Qual o seu nome?', validators= [DataRequired()])
  submit = SubmitField('Enviar')

# Rota função view
@app.route('/', methods=['GET', 'POST'])
def index():
  form = NameForm()
  if form.validate_on_submit():
    old_name = session.get('name') # antes da primeira submissão

    # Validação do envio do formulário (PRG)
    if old_name is not None and old_name != form.name.data:
      flash('Parece que você alterou seu nome')
    session['name'] = form.name.data # variável de sessão
    return redirect(url_for('index'))

  # Renderiza a página HTML com os dadso salvos na session
  return render_template('index.html', form=form, name=session.get('name'))