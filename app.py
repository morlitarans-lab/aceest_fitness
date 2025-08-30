from flask import Flask, request, jsonify, render_template

def create_app(test_config: dict | None = None):
    app = Flask(__name__)
    app.config.update({
        "TESTING": False,
    })
    if test_config:
        app.config.update(test_config)

    # In-memory store for simplicity (sufficient for assignment)
    app.workouts = []

    @app.get("/")
    def index():
        # Simple landing page with a form + list
        return render_template("index.html", workouts=app.workouts)

    @app.post("/workouts")
    def add_workout():
        data = request.get_json(silent=True) or request.form.to_dict()
        workout = (data.get("workout") or "").strip()
        duration_raw = (str(data.get("duration") or "")).strip()

        if not workout or not duration_raw:
            return jsonify({"error": "Both 'workout' and 'duration' are required"}), 400

        try:
            duration = int(duration_raw)
        except ValueError:
            return jsonify({"error": "'duration' must be an integer"}), 400

        entry = {"workout": workout, "duration": duration}
        app.workouts.append(entry)
        # Return created representation
        return jsonify(entry), 201

    @app.get("/workouts")
    def view_workouts():
        return jsonify({"count": len(app.workouts), "items": app.workouts}), 200

    @app.delete("/workouts")
    def clear_workouts():
        app.workouts.clear()
        return jsonify({"status": "cleared"}), 200

    return app

# Gunicorn entrypoint
app = create_app()
