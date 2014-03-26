from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


blogadm = Admin(app, name="Blog app")

from admin import CategoryView, PostView

blogadm.add_view(CategoryView(db.session))
blogadm.add_view(PostView(db.session))

from application import views
