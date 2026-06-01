import os
import sqlite3
from flask import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__)
app.secret_key="mysecretkey"
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
db_path=os.path.join(BASE_DIR,"quiz_app.db")
def init_db():
    conn=sqlite3.connect(db_path,timeout=10)
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS quiz_app(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,password TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS leaderboard(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,score INTEGER)""")
    conn.commit()
    conn.close()
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        return redirect(url_for('login'))
    return render_template('home.html')
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        conn=sqlite3.connect(db_path,timeout=10)
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS quiz_app(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,password TEXT)""")
        cursor.execute("INSERT INTO quiz_app(name,email,password) VALUES(?,?,?)",(name,email,password))
        conn.commit()
        print(os.path.abspath("quiz_app.db"))
        conn.close()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        conn=sqlite3.connect(db_path,timeout=10)
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM quiz_app WHERE email=? AND password=?", (email, password))
        user=cursor.fetchone()
        conn.close()
        if user:
            session["name"]=user[1]
            return redirect(url_for('quiz'))
        else:
            return "Invalid email or password"
    return render_template('login.html')

@app.route("/quiz",methods=["GET","POST"])
def quiz():
    if request.method=="POST":
        score=0
        q1=request.form["q1"]
        q2=request.form["q2"]
        q3=request.form["q3"]
        q4=request.form["q4"]
        q5=request.form["q5"]
        q6=request.form["q6"]
        q7=request.form["q7"]
        q8=request.form["q8"]
        q9=request.form["q9"]
        q10=request.form["q10"]
        if q1=="Python":
            score+=1
        if q2=="Flask":
            score+=1
        if q3=="input()":
            score+=1
        if q4==".py":
            score+=1
        if q5=="def":
            score+=1
        if q6=="#":
            score+=1
        if q7=="print()":
            score+=1
        if q8=="float":
            score+=1
        if q9=="int":
            score+=1
        if q10=="for":
            score+=1

        name=session.get("name","Guest") 
        conn=sqlite3.connect(db_path,timeout=10)
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS leaderboard(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,score INTEGER)""")
        cursor.execute("INSERT INTO leaderboard(name,score) VALUES(?,?)",(name,score))
        conn.commit()
        conn.close()
        return render_template('result.html',score=score)
    return render_template('quiz.html')

@app.route("/leaderboard")
def leaderboard():
    conn=sqlite3.connect(db_path,timeout=10)
    cursor=conn.cursor()
    cursor.execute("SELECT name,score FROM leaderboard ORDER BY score DESC")
    data=cursor.fetchall()
    conn.close()
    return render_template('leaderboard.html',data=data)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True,use_reloader=False)