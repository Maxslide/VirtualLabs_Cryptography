from flask import Flask, render_template, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from random import shuffle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template("index.html") #Called when the web app is just opened

@app.route('/Introduction')
def introduction():
    return render_template('Introduction.html') # Renders the Introduction page

@app.route('/Theory')
def Theory():
    return render_template('Theory.html') # Renders the Theory page

@app.route('/Objective')
def Objective():
    return render_template('Objective.html') # Renders the Objective page

@app.route('/Experiment')
def Experiment():
    return render_template('Experiment.html') # Renders the Exepriment page

@app.route('/Manual')
def Manual():
    return render_template('Manual.html') # Renders the Manual page

@app.route('/Quizzes') #renders the Quizzes page along with displaying the content of the database created
def Quizzes():
    db.drop_all()
    createDB() # Creates the database
    a = showDB() # Stores the database in a variable, in the form of a list
    shuffle(a)
    return render_template('Quizzes.html', Ques = a)

@app.route('/Procedure')
def Procedure():
    return render_template('Procedure.html') # Renders the procedure page

@app.route('/Further_Reading')
def Further_Reading():
    return render_template('Further_Reading.html') # Renders the Procedure page

#Q to be added to the database stored in the list form [Q,op1,op2,op3,op4,ans].

Question = [
    ["Which criterion ensures that we can’t find two messages that hash to the same digest?",
    "One-wayness",
    "Weak-collision-resistance",
    "Strong-collision-resistance",
    "None",
    "Weak-collision-resistance"],
    ["Which criterion Ensures that it must be extremely difficult or impossible to create the message if the message digest is given.",
    "One-wayness",
    "Weak-collision-resistance",
    "Strong-collision resistance",
    "None",
    "One-wayness"],
    ["Consider the function h: {0,1}8 -> {0,1}4. Suppose h(x) = x xmod 5 mod 16, x in [0, 255]. The collision in h occurs for.",
    "(1, 17)",
    "(2, 16)",
    "(1, 16)",
    "(2, 17)",
    "(1, 17)"],
    ["The Merkle-Damgard Transform is mainly useful for",
    "Converting any fixed-length collision resistant hash function to an arbitrary length collision resistant hash function",
    "Converting arbitrary length hash function to a fixed length hash function",
    "Constructing hash function from random function",
    "None",
    "Converting arbitrary length hash function to a fixed length hash function"],
    ["Q5",
    "51",
    "52",
    "53",
    "54",
    "52"],
    ["Q6",
    "61",
    "62",
    "63",
    "64",
    "63"],
    ["Q7",
    "71",
    "72",
    "73",
    "74",
    "74"],
    ["Q8",
    "81",
    "82",
    "83",
    "84",
    "82"]]


class Quiz(db.Model): # Defines the databse columns
    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    Ques = db.Column(db.String(500),nullable = False)
    Opt1 = db.Column(db.String(500),nullable = False)
    Opt2 = db.Column(db.String(500),nullable = False)
    Opt3 = db.Column(db.String(500),nullable = False)
    Opt4 = db.Column(db.String(500),nullable = False)
    ans = db.Column(db.String(500),nullable = False)


def createDB(): # Creates the database with the given definition
    db.create_all()
    for i in Question:
        new_ent = Quiz(Ques = i[0], Opt1 = i[1], Opt2 = i[2], Opt3 = i[3], Opt4 = i[4], ans = i[5])
        db.session.add(new_ent)
        db.session.commit()
    return


def showDB(): # returns the content of the database in a list form
    ent = Quiz.query.all()
    a = []
    for i in ent:
        b = {
            'Q': i.Ques,
            'o1': i.Opt1,
            'o2': i.Opt2,
            'o3': i.Opt3,
            'o4': i.Opt4,
            'ans': i.ans
        }
        a.append(b)
    return a

if __name__ == "__main__":
    app.run(debug=True)



















