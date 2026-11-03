from flask import jsonify


def register_routes(app):

    employees = [
        {"id": 1, "name": "John", "department": "DevOps"},
        {"id": 2, "name": "David", "department": "Development"},
        {"id": 3, "name": "Sarah", "department": "Testing"}
    ]

    @app.route("/")
    def home():
        return jsonify({
            "application": "Employee Management System",
            "version": "1.0.0",
            "status": "running"
        })

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.route("/employees")
    def employees_list():
        return jsonify({
            "employees": employees,
            "total": len(employees)
        }), 200
