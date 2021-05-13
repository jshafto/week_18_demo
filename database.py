from dotenv import load_dotenv
load_dotenv()

from app import app, db               # noqa
from app.models import Widget, Store  # noqa

with app.app_context():
    db.drop_all()
    # db.create_all()

    # new_widget = Widget(color="red")
    # two_widget = Widget(color="blue")
    # three_widget = Widget(color="rpurple")
    # four_widget = Widget(color="rorange")
    # five_widget = Widget(color="chartreuse")
    # db.session.add(new_widget)
    # db.session.add(two_widget)
    # db.session.add(three_widget)
    # db.session.add(four_widget)
    # db.session.add(five_widget)

    # store_one = Store(name="Marni's Widget Shoppe")
    # store_two = Store(name="Ed's Wholesale")

    # db.session.add(store_one)
    # db.session.add(store_two)

    # print(new_widget.stores, "-------")
    # new_widget.stores.append(store_one)
    # print(new_widget.stores, "-------")

    # store_two.widgets.append(two_widget)
    # print(store_two.widgets, "-------")

    # store_two.widgets = [four_widget, five_widget]
    # print(store_two.widgets, "-------")

    # db.session.commit()
    # print(store_two.widgets, "-------")

    # store_two.widgets.remove(four_widget)
    # db.session.add(store_two)
    # db.session.commit()
    # print(store_two.widgets, "-------")

    # widgets = Widget.query.filter(Widget.color == "blue").all()
    # print([widget.color for widget in widgets])

    # my_widget = Widget.query.filter(Widget.color.ilike("r%")).first()
    # print(my_widget.id)
