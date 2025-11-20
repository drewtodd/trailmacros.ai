# TrailMacros

A lightweight nutrition tracking and analysis tool for backpacking, lightweight travel, and fitness goals.

## Features

- **Food Lookup & Comparison**: Search and analyze foods by calories, protein, carbs, and fat
- **Backpacking Optimization**: Identify calorie-dense, low-weight foods for extended trips
- **Personal Food Database**: Create and manage your own food entries
- **Macronutrient Analysis**: View detailed nutritional breakdowns and calorie-to-weight ratios
- **Mobile-First Design**: Fully responsive, WCAG 2.1 AA compliant interface
- **Future-Ready API**: RESTful backend designed for easy migration to iOS/Android

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, Tailwind CSS, htmx
- **Database**: SQLite (MVP) → PostgreSQL (future)
- **Accessibility**: WCAG 2.1 AA compliant

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/drewtodd/trailmacros.ai.git
cd trailmacros.ai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r backend/requirements.txt
```

4. Run the app:
```bash
export FLASK_ENV=development
python backend/app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
trailmacros.ai/
├── backend/
│   ├── app.py              # Flask application
│   ├── config.py           # Configuration settings
│   ├── models.py           # SQLAlchemy models
│   ├── routes/
│   │   └── foods.py        # Food CRUD endpoints
│   ├── database.db         # SQLite database
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── templates/
│   │   ├── base.html       # Base template
│   │   ├── index.html      # Home page
│   │   ├── add_food.html   # Add food form
│   │   ├── edit_food.html  # Edit food form
│   │   └── partials/
│   │       └── food_card.html  # Food card component
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript (htmx, vanilla JS)
│   └── assets/             # Images, icons, etc.
└── README.md
```

## API Endpoints

### Foods

- `GET /api/foods` - List all foods (with filtering)
- `GET /api/foods/<id>` - Get a specific food
- `POST /api/foods` - Create a new food
- `PUT /api/foods/<id>` - Update a food
- `DELETE /api/foods/<id>` - Delete a food

### Query Parameters

- `search=<string>` - Search by food name
- `category=<string>` - Filter by category
- `source=<string>` - Filter by source (personal, usda, brand)

## Roadmap

### MVP (Current)
- [x] Food CRUD functionality
- [x] Food lookup and comparison
- [x] Calorie-to-weight ratio for backpacking
- [x] Single-user interface

### Phase 2
- [ ] User authentication & accounts
- [ ] Multi-user support
- [ ] Meal logging and tracking
- [ ] Macro targets & goals
- [ ] USDA FoodData Central integration

### Phase 3
- [ ] Recipes and meal planning
- [ ] Shopping lists
- [ ] Native iOS/Android apps
- [ ] QR code scanning
- [ ] Photo-based meal tracking

## Development

### Running Tests (Future)
```bash
pytest backend/
```

### Database Migrations (Future)
```bash
flask db upgrade
```

## Accessibility

This app is built with WCAG 2.1 AA compliance in mind:

- Semantic HTML structure
- Proper heading hierarchy
- ARIA labels and roles
- Keyboard navigation support
- Color contrast ratios (4.5:1 for text, 3:1 for UI components)
- Focus indicators
- Skip to main content link

## Contributing

This is a personal project, but feel free to reach out with suggestions or feedback!

## License

MIT License - feel free to use this as a template for your own projects.

## Support

For issues, questions, or feedback, please open an issue on GitHub.

---

**Built with ❤️ for outdoor enthusiasts and fitness-focused individuals.**
