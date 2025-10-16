from flask import Flask
from routes.pages.home import home_bp
from routes.pages.room import room_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(room_bp)

if __name__ == '__main__':
    app.run(debug=True)

