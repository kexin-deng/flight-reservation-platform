import os

from flask import Flask

try:
    from .general import general_bp
    from .airline_staff import airline_staff_bp
    from .customer import customer_bp
    from .booking_agent import booking_agent_bp
except ImportError:
    from general import general_bp
    from airline_staff import airline_staff_bp
    from customer import customer_bp
    from booking_agent import booking_agent_bp


# Web App Initialization with Configured MySQL Connection
class WebApp:
    def __init__(self):
        self.flask_app = Flask(__name__)
        self.flask_app.register_blueprint(general_bp)
        self.flask_app.register_blueprint(airline_staff_bp)
        self.flask_app.register_blueprint(customer_bp)
        self.flask_app.register_blueprint(booking_agent_bp)
        self.flask_app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

    def run(self):
        port = int(os.environ.get("PORT", 8000))
        self.flask_app.run(host="0.0.0.0", port=port)


def create_app():
    return WebApp().flask_app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

