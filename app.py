from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import joblib
from util import get_counseling_tips

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Hardcoded credentials (replace with DB later if needed)
USER_CREDENTIALS = {
    "admin": "password123",
    "child": "emo123"
}

# Load model and label encoder
model = joblib.load("model/emotion_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        session['user'] = username
        return redirect('/index')
    else:
        flash("Invalid name or password. Please try again.")
        return redirect('/')

@app.route('/index')
def home():
    if 'user' not in session:
        return redirect('/')
    return render_template("index.html")

@app.route('/emotion')
def emotion_page():
    if 'user' not in session:
        return redirect('/')
    return render_template("emotion.html")

@app.route('/quiz')
def quiz_page():
    if 'user' not in session:
        return redirect('/')
    return render_template("quiz.html")

@app.route('/consult_bot')
def consult_bot():
    if 'user' not in session:
        return redirect('/')
    emotion = request.args.get("emotion", "Happy")
    return render_template("consult_bot.html", emotion=emotion)

@app.route('/game')
def game_page():
    if 'user' not in session:
        return redirect('/')
    emotion = request.args.get("emotion", "Happy")
    return render_template(f"game_{emotion.lower()}.html")

@app.route('/video')
def video():
    if 'user' not in session:
        return redirect('/')
    emotion = request.args.get("emotion", "Happy")
    return render_template("video.html", emotion=emotion.capitalize())

@app.route('/report')
def report():
    if 'user' not in session:
        return redirect('/')
    emotion = request.args.get("emotion", "Happy")
    score = request.args.get("score", 0)
    return render_template("report.html", emotion=emotion, score=score)

@app.route('/counsel', methods=['POST'])
def counsel():
    source = request.form.get('source')
    language = request.form.get("language", "English")

    if source == "quiz":
        try:
            input_data = [
                int(request.form.get("q1")),
                int(request.form.get("q2")),
                int(request.form.get("q3")),
                int(request.form.get("q4")),
                int(request.form.get("q5")),
                int(request.form.get("q6")),
                0, 0
            ]
            prediction = model.predict([input_data])[0]
            emotion = label_encoder.inverse_transform([prediction])[0]
        except:
            emotion = "Numb"
    else:
        emotion = request.form.get("emotion", "Numb")

    return redirect(url_for('consult_bot', emotion=emotion))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
