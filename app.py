from flask import Flask, render_template, request, session, redirect, url_for
import random
from hangman_word import word_list
from hangman_art import stages, logo

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'lives' not in session:
        session['lives'] = 6
        session['word'] = random.choice(word_list)
        session['display'] = ['_'] * len(session['word'])
        session['guesses'] = []

    message = ""
    if request.method == 'POST':
        guess = request.form['guess'].lower()
        if guess in session['guesses']:
            message = f"You already guessed '{guess}'."
        else:
            session['guesses'].append(guess)
            if guess in session['word']:
                for i, c in enumerate(session['word']):
                    if c == guess:
                        session['display'][i] = guess
                if '_' not in session['display']:
                    message = "🎉 You win!"
            else:
                session['lives'] -= 1
                if session['lives'] == 0:
                    message = f"💀 You lost! The word was '{session['word']}'."

    return render_template('index.html',
                           logo=logo,
                           display=' '.join(session['display']),
                           guesses=session['guesses'],
                           lives=session['lives'],
                           stage=stages[session['lives']],
                           message=message)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
