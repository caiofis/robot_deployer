import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db

ALLOWED_EXTENSIONS = {'gz'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)

@main.errorhandler(413)
def too_large(e):
    flash('File is too large')
    return redirect(url_for('main.upload'))

@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('main.upload'))

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('main.upload'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('main.index'))

        flash('File extention not allowed')
        return redirect(url_for('main.upload'))
    if request.method == 'GET':
        return render_template("upload.html")
