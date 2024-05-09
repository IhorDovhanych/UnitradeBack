import os
import sys
from a2wsgi import ASGIMiddleware
from app.main import app


sys.path.insert(0, os.path.dirname(__file__))

application = ASGIMiddleware(app)