from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from models import db, Food

# API Blueprint for JSON endpoints
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Pages Blueprint for HTML page routes
pages_bp = Blueprint('pages', __name__)

# ===== API Endpoints (JSON) =====

@api_bp.route('/foods', methods=['GET'])
def get_foods():
    """Get all foods (with optional filtering)"""
    query = Food.query

    # Optional filters
    category = request.args.get('category')
    source = request.args.get('source')
    search = request.args.get('search')

    if category:
        query = query.filter_by(category=category)
    if source:
        query = query.filter_by(source=source)
    if search:
        query = query.filter(Food.name.ilike(f'%{search}%'))

    foods = query.all()
    return jsonify([food.to_dict() for food in foods])

@api_bp.route('/foods/<int:food_id>', methods=['GET'])
def get_food(food_id):
    """Get a single food by ID"""
    food = Food.query.get_or_404(food_id)
    return jsonify(food.to_dict())

@api_bp.route('/foods', methods=['POST'])
def create_food():
    """Create a new food"""
    data = request.get_json()

    # Validation
    if not data.get('name') or not data.get('calories'):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check for duplicate name
    if Food.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'Food already exists'}), 409

    food = Food(
        name=data['name'],
        description=data.get('description'),
        calories=data['calories'],
        protein=data.get('protein', 0),
        carbs=data.get('carbs', 0),
        fat=data.get('fat', 0),
        weight_raw=data.get('weight_raw'),
        weight_prepared=data.get('weight_prepared'),
        source=data.get('source', 'personal'),
        category=data.get('category'),
        brand=data.get('brand'),
    )

    db.session.add(food)
    db.session.commit()

    return jsonify(food.to_dict()), 201

@api_bp.route('/foods/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    """Update a food"""
    food = Food.query.get_or_404(food_id)
    data = request.get_json()

    # Update fields
    food.name = data.get('name', food.name)
    food.description = data.get('description', food.description)
    food.calories = data.get('calories', food.calories)
    food.protein = data.get('protein', food.protein)
    food.carbs = data.get('carbs', food.carbs)
    food.fat = data.get('fat', food.fat)
    food.weight_raw = data.get('weight_raw', food.weight_raw)
    food.weight_prepared = data.get('weight_prepared', food.weight_prepared)
    food.source = data.get('source', food.source)
    food.category = data.get('category', food.category)
    food.brand = data.get('brand', food.brand)

    db.session.commit()
    return jsonify(food.to_dict())

@api_bp.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food_api(food_id):
    """Delete a food"""
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return '', 204

# ===== Page Routes (HTML) =====

@pages_bp.route('/', methods=['GET'])
def index():
    """Home page - food lookup and comparison"""
    foods = Food.query.all()
    return render_template('index.html', foods=foods)

@pages_bp.route('/add', methods=['GET', 'POST'])
def add_food():
    """Add food form"""
    if request.method == 'POST':
        data = request.form
        food = Food(
            name=data['name'],
            description=data.get('description'),
            calories=float(data['calories']),
            protein=float(data.get('protein', 0)),
            carbs=float(data.get('carbs', 0)),
            fat=float(data.get('fat', 0)),
            weight_raw=float(data['weight_raw']) if data.get('weight_raw') else None,
            weight_prepared=float(data['weight_prepared']) if data.get('weight_prepared') else None,
            source=data.get('source', 'personal'),
            category=data.get('category'),
            brand=data.get('brand'),
        )
        db.session.add(food)
        db.session.commit()
        return redirect(url_for('pages.index'))

    return render_template('add_food.html')

@pages_bp.route('/edit/<int:food_id>', methods=['GET', 'POST'])
def edit_food(food_id):
    """Edit food form"""
    food = Food.query.get_or_404(food_id)

    if request.method == 'POST':
        data = request.form
        food.name = data['name']
        food.description = data.get('description')
        food.calories = float(data['calories'])
        food.protein = float(data.get('protein', 0))
        food.carbs = float(data.get('carbs', 0))
        food.fat = float(data.get('fat', 0))
        food.weight_raw = float(data['weight_raw']) if data.get('weight_raw') else None
        food.weight_prepared = float(data['weight_prepared']) if data.get('weight_prepared') else None
        food.source = data.get('source', 'personal')
        food.category = data.get('category')
        food.brand = data.get('brand')
        db.session.commit()
        return redirect(url_for('pages.index'))

    return render_template('edit_food.html', food=food)

@pages_bp.route('/delete/<int:food_id>', methods=['POST'])
def delete_food_html(food_id):
    """Delete food (HTML form submission)"""
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return redirect(url_for('pages.index'))
