from flask import Flask, render_template, redirect, session, jsonify
from flask_migrate import Migrate
from app.config import Config
from app.forms.fun_form import WidgetForm
from app.models import db, Widget

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)


@app.route("/")
def index():
    return render_template("home.html", title="Homepage")


@app.route('/form')
def view_form():
    form = WidgetForm()
    return render_template('form.html', form=form)


@app.route('/form', methods=["POST"])
def process_form():
    form = WidgetForm()
    # attempt to validate the form
    if form.validate_on_submit():
        # get the values that i want from the form
        # print(form.data)
        data = {"color": "pink"}
        color = form.data.get("color", None)
        widget = Widget(**data)
        db.session.add(widget)
        db.session.commit()

        return redirect(f"/form_data/{widget.id}")
    return render_template("form.html", form=form)


@app.route("/form_data/<int:id>")
def display_form(id):
    widget = Widget.query.get(id)
    print(widget)
    return render_template("form_data.html", color=widget.color)


@app.route("/form_json/<int:id>")
def display_json(id):
    widget = Widget.query.get(id)
    return widget.to_dict()


@app.route("/all_widgets_json")
def display_all_widgets():
    widgets = Widget.query.all()
    return {"widgets": [widget.to_dict() for widget in widgets]}
