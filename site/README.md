# Flask Application

This project is a Flask web application designed to manage and display mathematical exercises. It utilizes SQLAlchemy for database interactions and follows a structured approach to separate concerns within the application.

## Project Structure

```
flask-app
├── src
│   ├── app
│   │   ├── __init__.py       # Initialize the Flask app and database
│   │   ├── models.py         # Data models for exercises
│   │   ├── routes.py         # HTTP route handlers
│   │   └── populate_db.py    # Script to populate the database
│   ├── templates
│   │   └── index.html        # Main HTML template for displaying exercises
│   └── static
│       ├── css               # CSS files for styling
│       └── js                # JavaScript files for client-side functionality
├── migrations                # Database migration files
├── instance
│   └── config.py             # Instance-specific configuration
├── venv                      # Virtual environment
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd flask-app
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the environment variables in the `.env` file.

## Database Setup

1. Configure your database connection in `instance/config.py`.
2. Run migrations to set up the database schema:
   ```sh
   flask db upgrade
   ```

## Database Population

The application requires initial data to function properly. You can populate the database using one of the following methods:

1. Using the provided script:
   ```sh
   python src/app/populate_db.py
   ```

2. Manually using the Flask shell:
   ```sh
   flask shell
   >>> from app.models import Exercice, db
   >>> # Create and add sample exercises
   >>> db.session.commit()
   ```

3. Import from JSON or CSV:
   ```sh
   flask import-data --file path/to/exercises.json
   ```

## Running the Application

To start the Flask application, run:
```sh
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to view the list of exercises.
- Use the provided routes to filter and interact with the exercises.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Converting Latex to SVG

Use the following command : dvisvgm --libgs=/opt/local/lib/libgs.dylib SVGFilename.dvi
Add this in the SVG to be able to center it on the page : style="display: block; margin: 0 auto;"
