from flask import Flask
from task_routes import task_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(task_blueprint, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)