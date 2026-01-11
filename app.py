from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ---------------- FIREBASE INIT ----------------
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# ---------------- FRAUD LOGIC ----------------
def analyze_transaction(amount, time, device, frequency):
    score = 0
    reasons = []

    if amount > 10000:
        score += 40
        reasons.append("High transaction amount")

    if time >= "22:00":
        score += 30
        reasons.append("Late night transaction")

    if device == "new":
        score += 20
        reasons.append("New device")

    if frequency > 5:
        score += 10
        reasons.append("High frequency")

    if score > 70:
        status = "High Risk"
    elif score > 30:
        status = "Medium Risk"
    else:
        status = "Safe"

    return status, score, reasons

# ---------------- API: ANALYZE (POST) ----------------
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    result_status, score, reasons = analyze_transaction(
        data["amount"],
        data["time"],
        data["device"],
        data["frequency"]
    )

    transaction = {
        "upi_id": data["upi_id"],
        "amount": data["amount"],
        "time": data["time"],
        "location": data["location"],
        "device": data["device"],
        "frequency": data["frequency"],
        "risk_status": result_status,
        "risk_score": score,
        "reasons": reasons,
        "created_at": datetime.now()
    }

    db.collection("transactions").add(transaction)

    return jsonify({
        "risk_status": result_status,
        "risk_score": f"{score}%",
        "reasons": ", ".join(reasons)
    })

# ---------------- API: FETCH TRANSACTIONS (GET) ----------------
@app.route("/transactions", methods=["GET"])
def get_transactions():
    try:
        docs = db.collection("transactions").stream()  # Simplified: removed order_by to avoid indexing issues
        result = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            result.append(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Returns error details if Firebase fails

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)