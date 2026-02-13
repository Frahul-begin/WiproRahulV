from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

patients = []

# -------------------------
# GET All Patients
# -------------------------
@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify(patients), 200


# -------------------------
# POST Register Patient
# -------------------------
@app.route('/api/patients', methods=['POST'])
def register_patient():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    patients.append(data)
    return jsonify(data), 201


# -------------------------
# GET Patient by Index
# -------------------------
@app.route('/api/patients/<int:index>', methods=['GET'])
def get_patient(index):
    if index < len(patients):
        return jsonify(patients[index]), 200
    return jsonify({"error": "Patient not found"}), 404


# -------------------------
# PUT Update Patient
# -------------------------
@app.route('/api/patients/<int:index>', methods=['PUT'])
def update_patient(index):
    if index < len(patients):
        data = request.get_json()
        patients[index].update(data)
        return jsonify(patients[index]), 200
    return jsonify({"error": "Patient not found"}), 404


# -------------------------
# Web Page
# -------------------------
@app.route('/')
def home():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
