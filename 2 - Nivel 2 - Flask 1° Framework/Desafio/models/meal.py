from database import db

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(80), nullable=False)
  dateTime = db.Column(db.String(80), nullable=False)
  isDiet = db.Column(db.Boolean, default=False)
  def to_dict(self):
    return {      
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'dateTime': self.dateTime,
      'isDiet': self.isDiet
    }