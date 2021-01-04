from .models import Gift
from ariadne import convert_kwargs_to_snake_case

def resolve_gifts(obj, info):
    try:
        gifts = [gift.to_dict() for gift in Gift.query.all()]
        payload = {
            "success": True,
            "gifts": gifts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_gift(obj, info, id):
    try:
        gift = Gift.query.get(id)
        payload = {
            "success": True,
            "gift": gift.to_dict()
        }

    except AttributeError:  # gift not found
        payload = {
            "success": False,
            "errors": [f"Gift matching id {id} not found"]
        }

    return payload