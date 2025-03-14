from flask import Flask
from task_routes import task_blueprint

app = Flask(__name__)
app.register_blueprint(task_blueprint, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)