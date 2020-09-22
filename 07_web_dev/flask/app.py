from flask import Flask, render_template, redirect, url_for, request, abort, jsonify
from datetime import datetime

import sys

sys.path.append(".")

from model import db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
    # first arguments is name of template file
    # other arguments are data passed to the template context
    # templates should be in folder /templates
    return render_template(
        "welcome.html",
        cards=db)


@app.route("/date", methods=["GET", "POST"])
def date():
    return "This page was served at " + str(datetime.now())


counter = 0


@app.route("/count_views", methods=["GET", "POST"])
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times"


@app.route("/card/<int:index>", methods=["GET", "POST"])
def card_view(index):
    try:
        card = db[index]
        return render_template(
            "card.html",
            card=card,
            index=index,
            max_index=len(db) - 1
        )
    except IndexError:
        abort(404)


@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # process submit
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        return redirect(url_for('card_view', index=len(db) - 1))
    else:
        return render_template("add_card.html")


@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            # save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)


# RESTful API
@app.route("/api/card/")
def api_card_list():
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
