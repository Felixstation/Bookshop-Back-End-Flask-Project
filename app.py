from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/project'
app.config['SECRET_KEY'] = 'project'



from controllers import *
from extensions import *
from models import *


if '__name__' == '__main__':
    app.init_app(db)
    app.init_app(migrate)




















# books = {
#     1 : {
#         'id' : 1,
#         'author' : 'Deniel Chidiak',
#         'book' : 'Kim Deyir ki Bacarmazsan?',
#         'price' : '15 $',
#         'old_price' : '20 $',
#         'images' : 'book1.jpeg',
#         'book_about' : 'Famous Deniel Chidiak book',
#         'stock' : 5,
#         'Language' : 'AZE'
#     },
#     2 :{
#         'id' : 2,
#         'author' : 'Sabahattin Ali',
#         'book' : 'Kürk Mantolu Madonna',
#         'price' : '20 $',
#         'old_price' : '25 $',
#         'images' : 'book2.jpeg',
#         'book_about' : 'Sabahattin Ali"s book',
#         'stock' : 6,
#         'Language' : 'TR'
#     },
#     3 :{
#         'id' : 3,
#         'author' : 'Luiza Hey',
#         'book' : 'Sən Həyatını Yaxşılaşdıra Bilərsən!',
#         'price' : '10 $',
#         'old_price' : '12 $',
#         'images' : 'book3.jpeg',
#         'book_about' : 'Some Description',
#         'stock' : 10,
#         'Language' : 'AZE'
#     },
# }

