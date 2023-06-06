from app import app
from flask import render_template , request , redirect ,url_for
from models import Book , Genre , Lang , Comments , User
from forms import CommentForm , RegisterForm , LoginForm
from extensions import db
from werkzeug.security import generate_password_hash
from flask_login import login_user  ,logout_user ,login_required



@app.route("/register" , methods = ['GET' , 'POST'])
def registry():
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.form)

        if form.validate_on_submit():
            user = User(
                name = form.name.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data)
            )
            
            db.session.add(user)
            db.session.commit()
        return redirect("/login")
    return render_template('register.html' , form = form)



@app.route("/login" , methods = ['GET' , 'POST'])
def LoGin():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        user = User.query.filter_by(name = form.name.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")

    return render_template('login.html' , form = form)

@app.route("/logout")
@login_required
def log_out():
    logout_user()
    return redirect('/')



@app.route("/")
def home():
    books = Book.query.all()
    return render_template('index.html' , book = books)



@app.route('/book/<int:id>' , methods = ['GET', 'POST'])
def book_about(id):
    books = Book.query.filter_by(id = id).first()
    genre = Genre.query.filter_by(id = books.genre).first()
    lang = Lang.query.filter_by(id = books.language).first()
    form = CommentForm(formdata=None)
    comments = Comments.query.filter_by(Book = books.id)
    count= Comments.query.filter_by(Book = books.id).count()
    if request.method == 'POST':
        form = CommentForm(request.form)
        
        if form.validate_on_submit():
            comment = Comments(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data,
                Book=books.id
              
            )

            db.session.add(comment)
            db.session.commit()

        form = CommentForm(formdata=None)
    return render_template('book.html' , book = books , genre = genre , lang = lang , form = form , comment = comments,count=count)

    
    
