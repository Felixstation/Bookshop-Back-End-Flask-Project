from extensions import db , login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash , generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin , db.Model):
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    name = db.Column(db.String(20) , nullable = False)
    email = db.Column(db.String(100) , nullable = False)
    password = db.Column(db.String(255) , nullable = False)
    

    def __init__(self , name , email , password):
        self.name = name
        self.email = email
        self.password = password

    def check_password(self , password):
        return check_password_hash(self.password , password)

    def __repr__(self):
       return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()



class Genre(db.Model):
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    genre = db.Column(db.String(10), nullable = False)
    Book = db.relationship('Book', backref = 'Genre')

    def __init__(self , genre):
        self.genre = genre

    def __repr__(self):
        return self.genre

    def save(self):
        db.session.add(self)
        db.session.commit()


class Lang(db.Model):
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    lang_name = db.Column(db.String(15) , nullable = True)
    lang_code = db.Column(db.String(5) , nullable = True)
    Book = db.relationship('Book', backref = 'Lang')
    
    def __init__(self , lang_name , lang_code):
        self.lang_name = lang_name
        self.lang_code = lang_code

    def __repr__(self):
        return self.lang_name
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Book(db.Model):
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    title = db.Column(db.String(50) , nullable = False)
    author = db.Column(db.String(50) , nullable = False)
    price = db.Column(db.Integer , nullable = False)
    description = db.Column(db.String(255)  , nullable = True)
    image_url = db.Column(db.String(100) , nullable = False)
    stock = db.Column(db.Integer , nullable = False)
    genre = db.Column(db.Integer , db.ForeignKey('genre.id') , nullable = False)
    language = db.Column(db.Integer , db.ForeignKey('lang.id'), nullable = False)
    publish_date = db.Column(db.DateTime , default = datetime.utcnow)
    
    
    def __init__(self, title ,author , price , description , image_url , stock , genre , language ):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.genre = genre
        self.language = language

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


class Comments(db.Model):
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(50))
    message = db.Column(db.String(255))
    date = db.Column(db.DateTime , default = datetime.utcnow)
    Book = db.Column(db.Integer , db.ForeignKey('book.id'))


    def __init__(self, name , email , message , Book):
        self.name = name
        self.email = email
        self.message = message
        self.Book = Book

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()