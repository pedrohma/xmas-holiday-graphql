from main import db
from datetime import datetime

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    received = db.Column(db.Boolean, default=False)
    url = db.Column(db.String)
    date_created = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "received": self.received,
            "description": self.description,
            "url": self.url,
            "date_created": str(self.date_created)
        }