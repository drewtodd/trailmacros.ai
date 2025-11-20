from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Food(db.Model):
    """Food item model for nutrition tracking"""
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=True)

    # Nutritional data (per 100g)
    calories = db.Column(db.Float, nullable=False)  # kcal per 100g
    protein = db.Column(db.Float, nullable=False)   # grams per 100g
    carbs = db.Column(db.Float, nullable=False)     # grams per 100g
    fat = db.Column(db.Float, nullable=False)       # grams per 100g

    # Weight metadata
    weight_raw = db.Column(db.Float, nullable=True)    # raw/unprepared weight in grams
    weight_prepared = db.Column(db.Float, nullable=True)  # prepared/cooked weight in grams

    # Source/category
    source = db.Column(db.String(50), default='personal', index=True)  # 'personal', 'usda', 'brand'
    category = db.Column(db.String(100), nullable=True, index=True)  # 'protein', 'carb', 'snack', etc.
    brand = db.Column(db.String(255), nullable=True)  # for branded items

    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convert model to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'calories': self.calories,
            'protein': self.protein,
            'carbs': self.carbs,
            'fat': self.fat,
            'weight_raw': self.weight_raw,
            'weight_prepared': self.weight_prepared,
            'source': self.source,
            'category': self.category,
            'brand': self.brand,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    def __repr__(self):
        return f"<Food {self.name}>"
