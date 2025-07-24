from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Vartotojas, Irasas
from . import db
from datetime import datetime

main = Blueprint('main', __name__)  # ← ŠITAS turi būti

@main.route('/')
def index():
    return redirect(url_for('login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        el_pastas = request.form['el_pastas']
        slaptazodis = request.form['slaptazodis']
        vart = Vartotojas.query.filter_by(el_pastas=el_pastas).first()
        if vart and vart.slaptazodis == slaptazodis:
            login_user(vart)
            return redirect(url_for('main.irasai'))
        else:
            flash('Neteisingas el. paštas arba slaptažodis')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@main.route('/irasai')
@login_required
def irasai():
    visi = Irasas.query.filter_by(vartotojas_id=current_user.id).all()
    return render_template('irasai.html', irasai=visi)
