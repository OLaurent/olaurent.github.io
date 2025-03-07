# Flask Application

This project is a Flask web application designed to manage and display mathematical exercises. It utilizes SQLAlchemy for database interactions and follows a structured approach to separate concerns within the application.

## Project Structure

```
flask-app
├── src
│   ├── app.py               # Entry point of the Flask application
│   ├── models.py            # Data models for exercises
│   ├── routes.py            # HTTP route handlers
│   ├── templates
│   │   └── index.html       # Main HTML template for displaying exercises
│   └── static
│       ├── css              # CSS files for styling
│       └── js               # JavaScript files for client-side functionality
├── migrations                # Database migration files
├── instance
│   └── config.py            # Instance-specific configuration
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables in the `.env` file.

## Database Setup

1. Configure your database connection in `instance/config.py`.
2. Run migrations to set up the database schema:
   ```
   flask db upgrade
   ```

## Running the Application

To start the Flask application, run:
```
python src/app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to view the list of exercises.
- Use the provided routes to filter and interact with the exercises.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.