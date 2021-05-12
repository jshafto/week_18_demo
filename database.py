from dotenv import load_dotenv
load_dotenv()

from app import app, db              # noqa

with app.app_context():
    db.drop_all()
    db.create_all()
