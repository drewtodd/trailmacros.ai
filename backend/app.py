import os
import sys
from pathlib import Path

# Add backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify
from config import config
from models import db, Food

def calculate_macro_ratio(protein, carbs, fat):
    """Calculate macronutrient ratios (in percentages)"""
    total_cals = (protein * 4) + (carbs * 4) + (fat * 9)
    if total_cals == 0:
        return {'protein': 0, 'carbs': 0, 'fat': 0}
    return {
        'protein': round((protein * 4 / total_cals) * 100, 1),
        'carbs': round((carbs * 4 / total_cals) * 100, 1),
        'fat': round((fat * 9 / total_cals) * 100, 1),
    }

def calculate_calorie_to_weight(calories, weight_raw):
    """Calculate calorie-to-weight ratio for backpacking optimization"""
    if weight_raw and weight_raw > 0:
        return round(calories / weight_raw, 2)
    return None

def create_app(config_name='development'):
    """Application factory"""
    # Use absolute paths for templates and static files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, 'frontend', 'templates')
    static_dir = os.path.join(base_dir, 'frontend', 'assets')

    app = Flask(__name__,
                template_folder=template_dir,
                static_folder=static_dir,
                static_url_path='/assets')

    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize database
    db.init_app(app)

    # Register blueprints/routes
    from routes.foods import api_bp, pages_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(pages_bp)

    # Register template context processors for WCAG and utility functions
    @app.context_processor
    def inject_utilities():
        return {
            'macro_ratio': calculate_macro_ratio,
            'calorie_to_weight': calculate_calorie_to_weight,
        }

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    port = int(os.getenv('FLASK_PORT', 5001))
    app.run(debug=True, host='127.0.0.1', port=port)
