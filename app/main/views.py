from flask import render_template
from . import main
# from ..models import User,Comment
# from .forms import CommentForm


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
