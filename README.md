# Kahoot Flask App

This is a Flask web application inspired by Kahoot, allowing users to create and join game rooms using randomly generated codes.

## Project Structure

```
kahoot-flask-app
├── app.py                # Main entry point of the Flask application
├── routes                # Contains route definitions
│   ├── __init__.py      # Initializes the routes package
│   ├── home.py          # Defines the home page route
│   └── room.py          # Defines the room page route
├── static                # Contains static files
│   ├── css              # Contains CSS files
│   │   └── style.css    # Styles for the application
│   └── img              # Contains image files
│       └── background.jpg # Background image for the home page
├── templates             # Contains HTML templates
│   ├── home.html        # HTML structure for the home page
│   └── room.html        # HTML structure for the room page
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd kahoot-flask-app
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install Flask
   ```

3. **Run the application:**
   Execute the following command to start the Flask application:
   ```
   python app.py
   ```

4. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000` to access the home page.

## Usage

- On the home page, you can create a new room by clicking the "Create Room" button, which will redirect you to a new room with a randomly generated code.
- You can also enter a code provided by an existing room in the "Enter Code" text box to join that room.

## License

This project is licensed under the MIT License.