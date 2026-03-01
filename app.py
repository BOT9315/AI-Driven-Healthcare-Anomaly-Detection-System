from flask import Flask, render_template
from model import predict_anomaly
from data_generator import generate_data
from database import Session, PatientData

app = Flask(__name__)

@app.route("/")
def dashboard():
    session = Session()

    data = generate_data()
    severity = predict_anomaly(data)

    patient = PatientData(
        heart_rate=data[0],
        spo2=data[1],
        temperature=data[2],
        blood_pressure=data[3],
        severity=severity
    )

    session.add(patient)
    session.commit()

    records = session.query(PatientData).order_by(PatientData.id.desc()).limit(10).all()

    return render_template("dashboard.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)