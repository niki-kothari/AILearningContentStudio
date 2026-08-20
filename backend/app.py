from flask import Flask
from routes.auth_routes import auth_bp
from routes.roadmap_routes import roadmap_bp
from routes.content_routes import content_bp

app = Flask(__name__)

# register_blueprint() method is the core tool used to attach a Flask Blueprint—a modular set of routes, templates, and static files—to your main Flask application instance.
app.register_blueprint(auth_bp)
app.register_blueprint(roadmap_bp)
app.register_blueprint(content_bp)

if __name__ == "__main__":
    app.run(debug=True)

    