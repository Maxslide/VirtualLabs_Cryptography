from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Introduction')
def introduction():
    return render_template('Introduction.html')


@app.route('/Theory')
def introduction():
    return render_template('Theory.html')

@app.route('/Objective')
def introduction():
    return render_template('Objective.html')

@app.route('/Experiment')
def introduction():
    return render_template('Experiment.html')

@app.route('/Manual')
def introduction():
    return render_template('Manual.html')

@app.route('/Quizzes')
def introduction():
    return render_template('Quizzes.html')

@app.route('/Procedure')
def introduction():
    return render_template('Procedure.html')

@app.route('/Further_Reading')
def introduction():
    return render_template('Further_Reading.html')

if __name__ == "__main__":
    app.run(debug=True)
