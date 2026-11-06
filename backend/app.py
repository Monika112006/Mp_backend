
from flask import Flask, jsonify
from routes.prediction import prediction_bp

app = Flask(__name__)

# Register prediction routes
app.register_blueprint(prediction_bp)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Heart Disease Risk Estimator Backend",
        "status": "running"
    })


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "Heart Disease Risk Estimator API"
    })


if __name__ == "__main__":
    app.run(debug=True)
