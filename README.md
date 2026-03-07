AI-Driven Healthcare Anomaly Detection System

AI-Driven Healthcare Anomaly Detection System is an end-to-end real-time patient monitoring platform that detects abnormal patterns in vital signs and generates early alerts for healthcare professionals. It combines machine learning, real-time streaming, database storage, and interactive dashboards to improve patient safety.

🧩 Features

>Real-Time Monitoring: Tracks patient vitals like heart rate, blood pressure, SpO₂, and temperature.
>Anomaly Detection: Uses ML models like Autoencoder Neural Network and Isolation Forest to classify patient conditions as LOW, MEDIUM, or HIGH.
>Interactive Dashboard: Visualizes live and historical data using Flask and HTML templates.
>Email Alerts: Sends automatic notifications to healthcare administrators on critical anomalies.
>Database Storage: Stores patient records and anomaly events in PostgreSQL.

🛠 Technology Stack
Layer	Technology / Library
Backend	Python, Flask, SQLAlchemy
Machine Learning	TensorFlow / Keras, Scikit-learn
Database	PostgreSQL
Streaming	Apache Kafka (optional for live streaming)
Frontend	HTML, CSS, Bootstrap
Visualization	Flask Jinja2 Templates, Charts

Project Structure

AI_Healthcare_System/
├── app.py # Main Flask app

├── database.py # Database models and connection

├── anomaly_detection.py # ML anomaly detection code

├── requirements.txt # Dependencies

├── templates/
│ └── dashboard.html

├── static/
│ └── style.css



⚡Getting Started
1️⃣ Clone the repository

git clone https://github.com/BOT9315/AI_Healthcare_System.git
cd AI_Healthcare_System


2️⃣Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux / Mac

3️⃣Install dependencies
pip install -r requirements.txt

4️⃣Configure PostgreSQL
1.Create a database (example: healthcare_db)
2.Update database.py connection string:
DATABASE_URL = "postgresql://username:password@localhost:5432/healthcare_db"

5️⃣Run Flask server
python app.py


6️⃣Open in Browser
Visit:
http://127.0.0.1:5000


🧠How It Works

1.Data Ingestion: Patient vitals are streamed via Kafka or simulated CSV data.
2.Anomaly Detection: ML models calculate anomaly scores for each vital sign.
3.Storage & Alerts: Records are stored in PostgreSQL, and critical anomalies trigger email alerts.
4.Visualization: Flask renders dashboard templates showing all patient records and severity levels.

📦Dependencies
Flask
SQLAlchemy
psycopg2
TensorFlow / Keras
Scikit-learn
pandas
numpy

Install all using:
pip install -r requirements.txt

🚀Future Improvements
1.Add real-time Kafka streaming for live vitals
2.Integrate advanced deep learning models for better anomaly prediction
3.Deploy online using Heroku, AWS, or Azure
4.Add authentication and multi-user support for healthcare admins



THANKS FOR VISITING MY REPOSITORY......

👨‍💻 Author
Ankush Kumar
AI / Machine Learning Developer
===========================================================================================


