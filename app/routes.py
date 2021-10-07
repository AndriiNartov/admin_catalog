from flask import flash, redirect, render_template


from app import app
from app.services import auto_fill_in_database


@app.route('/')
def index():
    return render_template('/app/index.html')


@app.route('/admin/fill_db')
def fill_db():
    message, category = auto_fill_in_database()
    flash(message, category=category)
    return redirect('/admin')
