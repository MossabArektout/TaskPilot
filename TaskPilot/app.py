from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3 as sql
import re
from datetime import datetime
import pytz

app = Flask(__name__)

app.secret_key = 'Mossab'

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.template_folder = 'templates'


@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/")
def add():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/register", methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST':
        con = sql.connect("register.db")
        cur = con.cursor()

        username = request.form['username']
        password = request.form['password']


        cur.execute('SELECT * FROM register WHERE (Username, Password) = (?, ?)', (username, password))
        account = cur.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        elif not username:
            msg = 'Must Give username'
        elif not password:
            msg = 'Must Give Password'
        else:
            cur.execute('INSERT INTO register (Username, Password) VALUES (?, ?)', (username, password))
            con.commit()
            msg = 'You have successfully registered !'
            return render_template('signup.html', msg = msg)
    return render_template('signup.html', msg=msg)


@app.route("/signin")
def signin():
    return render_template("login.html")

@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        con = sql.connect("register.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM register WHERE Username = (?) AND Password = (?)', (username, password ))
        account = cur.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
            return redirect('/home')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


@app.route("/add")
def adding():
    return render_template('add.html')

@app.route('/addtask',methods=['GET', 'POST'])
def addtask():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        user_title = request.form["title"]
        user_desc = request.form["desc"]

        morocco_tz = pytz.timezone('Africa/Casablanca')
        morocco_datetime = datetime.now(tz=morocco_tz)
        date_format = '%d-%m-%Y %H:%M:%S'
        date_str = morocco_datetime.strftime(date_format)
        date_created = datetime.strptime(date_str, date_format)

        username = session["username"]

        con = sql.connect("register.db")
        cur = con.cursor()
        cur.execute("INSERT INTO tasks (title, desc, date_created, user_id) VALUES (?, ?, ?, ?)", (user_title, user_desc, date_created, username))
        con.commit()
        con.close()

    con = sql.connect("register.db")
    cur = con.cursor()
    username = session['username']
    cur.execute("SELECT * FROM tasks WHERE user_id = ?" ,(username,))
    all_items = cur.fetchall()
    return render_template("add.html", all_todos=all_items)

# Update route

@app.route("/update/<int:sno>", methods=["GET", "POST"])
def updatetask(sno):
    if request.method == "POST":
        user_title = request.form["title"]
        user_desc = request.form["desc"]

        con = sql.connect("register.db")
        cur = con.cursor()

        # Update the task in the database
        cur.execute("UPDATE tasks SET title=?, desc=? WHERE sno=?", (user_title, user_desc, sno))

        con.commit()
        con.close()
        return redirect("/addtask")

    con = sql.connect("register.db")
    cur = con.cursor()

    # Fetch the task to be updated
    cur.execute("SELECT * FROM tasks WHERE sno=?", (sno,))
    item = cur.fetchone()

    con.close()

    return render_template("update.html", todo=item)


# Delete route


@app.route('/delete/<int:sno>')
def deletetask(sno):
    con = sql.connect("register.db")
    cur = con.cursor()

    # Check if item with given sno exists
    #cur.execute("SELECT * FROM tasks WHERE title=?", (todo_id,))
    #item = cur.fetchone()

    # Delete the item
    cur.execute("DELETE FROM tasks WHERE sno=?", (sno,))
    con.commit()
    con.close()

    return redirect('/addtask')


@app.route('/logout')

def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
