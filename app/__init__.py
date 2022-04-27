from flask import Flask


from app.config import DevConfig

# initialize application

app = Flask (__name__,instance_relative_config = True)
app.config.from_object(DevConfig) 
app.config.from_pyfile('config.py')

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)

from app import views
from app import error

# from flask_bootstrap import Bootstrap