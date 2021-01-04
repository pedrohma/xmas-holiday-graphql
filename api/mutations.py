from datetime import datetime
from ariadne import convert_kwargs_to_snake_case
from api import db
from .models import Gift
from ariadne import MutationType

mutation = MutationType()

def resolve_create(obj, info, description, url):
    try:
        today = datetime.today().date()
        gift = Gift(
            description=description,
            url=url,
            date_created=today
        )
        db.session.add(gift)
        db.session.commit()
        payload = {
            "success": True,
            "gift": gift.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload