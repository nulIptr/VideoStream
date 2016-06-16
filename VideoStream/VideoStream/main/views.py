"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from . import main
from .logic import  getdata

@main.route('/')
def index():
    """Renders the home page."""
    l=getdata("")
    return render_template(
        'index.html',
        infolist=l,
    )

#@main.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@main.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
