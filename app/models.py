from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


widget_stores = db.Table(
    "widget_stores",
    db.Column(
        "widget_id", db.Integer, db.ForeignKey("widgets.id"), primary_key=True
    ),
    db.Column(
        "store_id", db.Integer, db.ForeignKey("stores.id"), primary_key=True
    )
)


class Widget(db.Model):
    __tablename__ = "widgets"
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50), nullable=False)
    # store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))

    stores = db.relationship(
        "Store",
        secondary=widget_stores,
        back_populates="widgets"
    )


class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    widgets = db.relationship(
        "Widget",
        secondary=widget_stores,
        back_populates="stores"
    )


class Juice(db.Model):
    __tablename__ = "juices"
    id = db.Column(db.Integer, primary_key=True)
    energy = db.Column(db.Integer)
    activities = db.Column(db.String(20))
    toys = db.Column(db.String(100))
