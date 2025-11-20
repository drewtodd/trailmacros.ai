"""
Seed the database with sample foods for testing.
Run with: python backend/seed_data.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models import db, Food

app = create_app()

# Sample foods optimized for backpacking and fitness
sample_foods = [
    # Backpacking staples (high calorie-to-weight ratio)
    {
        'name': 'Almonds',
        'description': 'Raw, unsalted almonds',
        'calories': 579,
        'protein': 21.2,
        'carbs': 21.6,
        'fat': 49.9,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'snack',
        'brand': None,
    },
    {
        'name': 'Peanut Butter',
        'description': 'Natural peanut butter, no added sugar',
        'calories': 588,
        'protein': 25.8,
        'carbs': 20.0,
        'fat': 50.0,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'snack',
        'brand': None,
    },
    {
        'name': 'Mountain House Freeze Dried Chicken',
        'description': 'Backpacking meal - freeze dried',
        'calories': 350,
        'protein': 35,
        'carbs': 30,
        'fat': 8,
        'weight_raw': 65,
        'weight_prepared': 180,
        'source': 'brand',
        'category': 'protein',
        'brand': 'Mountain House',
    },
    {
        'name': 'Trail Mix',
        'description': 'Almonds, raisins, chocolate chips',
        'calories': 500,
        'protein': 15.0,
        'carbs': 45.0,
        'fat': 28.0,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'snack',
        'brand': None,
    },
    {
        'name': 'Beef Jerky',
        'description': 'Lean beef jerky, no added sugar',
        'calories': 155,
        'protein': 32.0,
        'carbs': 3.0,
        'fat': 2.0,
        'weight_raw': 30,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'protein',
        'brand': None,
    },

    # Fitness/everyday nutrition
    {
        'name': 'Chicken Breast (cooked)',
        'description': 'Skinless, roasted',
        'calories': 165,
        'protein': 31.0,
        'carbs': 0.0,
        'fat': 3.6,
        'weight_raw': 100,
        'weight_prepared': 100,
        'source': 'personal',
        'category': 'protein',
        'brand': None,
    },
    {
        'name': 'Eggs',
        'description': 'Large egg, whole',
        'calories': 155,
        'protein': 13.0,
        'carbs': 1.1,
        'fat': 11.0,
        'weight_raw': 50,
        'weight_prepared': 50,
        'source': 'personal',
        'category': 'protein',
        'brand': None,
    },
    {
        'name': 'Greek Yogurt (plain)',
        'description': '0% fat, plain',
        'calories': 59,
        'protein': 10.0,
        'carbs': 3.3,
        'fat': 0.4,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'protein',
        'brand': None,
    },
    {
        'name': 'Brown Rice (cooked)',
        'description': 'Medium grain, cooked',
        'calories': 111,
        'protein': 2.6,
        'carbs': 23.0,
        'fat': 0.9,
        'weight_raw': 45,
        'weight_prepared': 150,
        'source': 'personal',
        'category': 'carbs',
        'brand': None,
    },
    {
        'name': 'Sweet Potato (baked)',
        'description': 'Medium, with skin',
        'calories': 103,
        'protein': 2.0,
        'carbs': 24.0,
        'fat': 0.1,
        'weight_raw': 100,
        'weight_prepared': 100,
        'source': 'personal',
        'category': 'carbs',
        'brand': None,
    },
    {
        'name': 'Banana',
        'description': 'Medium, raw',
        'calories': 89,
        'protein': 1.1,
        'carbs': 23.0,
        'fat': 0.3,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'carbs',
        'brand': None,
    },
    {
        'name': 'Broccoli (raw)',
        'description': 'Fresh, chopped',
        'calories': 34,
        'protein': 2.8,
        'carbs': 7.0,
        'fat': 0.4,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'snack',
        'brand': None,
    },
    {
        'name': 'Olive Oil',
        'description': 'Extra virgin',
        'calories': 884,
        'protein': 0.0,
        'carbs': 0.0,
        'fat': 100.0,
        'weight_raw': 100,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'fat',
        'brand': None,
    },
    {
        'name': 'Whey Protein Powder',
        'description': 'Vanilla flavor',
        'calories': 110,
        'protein': 24.0,
        'carbs': 2.0,
        'fat': 1.5,
        'weight_raw': 30,
        'weight_prepared': None,
        'source': 'personal',
        'category': 'protein',
        'brand': None,
    },
    {
        'name': 'Oats (dry)',
        'description': 'Rolled oats',
        'calories': 389,
        'protein': 16.7,
        'carbs': 66.3,
        'fat': 6.9,
        'weight_raw': 100,
        'weight_prepared': 300,
        'source': 'personal',
        'category': 'carbs',
        'brand': None,
    },
]

with app.app_context():
    # Clear existing foods
    Food.query.delete()

    # Add sample foods
    for food_data in sample_foods:
        food = Food(**food_data)
        db.session.add(food)

    db.session.commit()
    print(f"✓ Seeded {len(sample_foods)} foods into the database")
