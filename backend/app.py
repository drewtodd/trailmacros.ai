import os
from flask import Flask, render_template, request, jsonify
from config import config
from models import db, Food

def create_app(config_name='development'):
    """Application factory"""
    app = Flask(__name__,
                template_folder='../frontend/templates',
                static_folder='../frontend/assets',
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

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    app.run(debug=True, port=5000)
