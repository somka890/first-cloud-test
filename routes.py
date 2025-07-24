from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .models import Vartotojas
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return redirect(url_for("main.login"))

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        el_pastas = request.form["el_pastas"]
        slaptazodis = request.form["slaptazodis"]

        vart = Vartotojas.query.filter_by(el_pastas=el_pastas).first()

        if vart and vart.slaptazodis == slaptazodis:
            login_user(vart)
            return redirect(url_for("main.irasai"))
        else:
            flash("Neteisingas el. paštas arba slaptažodis.")

    return render_template("login.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/irasai")
@login_required
def irasai():
    return render_template("irasai.html")

# Šitas route prideda duomenų bazės lenteles
@main.route("/init-db")
def init_db():
    db.create_all()
    return "DB sukurta"
