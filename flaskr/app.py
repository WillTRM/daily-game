from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap5
from math import sqrt
import secrets
import phonotactics
import random
import vectors
import datetime

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)

today = datetime.date.today()
epoch = datetime.date(1970, 1, 1)
seed = (today - epoch).days
random.seed(seed)

goal_ipa = phonotactics.generate(random.randint(0, 10000000))
goal_word = phonotactics.to_latin(goal_ipa)
goal_vector = vectors.word_vector(goal_ipa)
pairs = []

class GuessForm(FlaskForm):
    name = StringField("Enter guess:")
    submit = SubmitField('Submit')

class RerollForm(FlaskForm):
    submit = SubmitField("Reroll word (debug)")

@app.route('/', methods = ["GET", "POST"])
def index():
    global goal_ipa, goal_word, goal_vector, pairs
    form = GuessForm()
    form2 = RerollForm()
    guess_similarity = -99999
    if form.validate_on_submit():
        guess = form.name.data
        guess_vector = vectors.word_vector(guess)
        guess_similarity = vectors.similarity(goal_vector, guess_vector)
        pairs.append((guess, guess_similarity))
        # print(guess)
    # if form2.validate_on_submit():
    #     goal_ipa = phonotactics.generate(random.randint(0, 10000000))
    #     goal_word = phonotactics.to_latin(goal_ipa)
    #     goal_vector = vectors.word_vector(goal_ipa)
        # mask = [random.randint(0, 1) for x in range(5)]

    return render_template('index.html', goal_word = goal_word, goal_ipa = "".join(goal_ipa), goal_vector = goal_vector, form = form, reroll_form = form2, pairs = pairs)

if __name__ == '__main__':
    app.run(debug = True)