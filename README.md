
# GramArogya - Rural Healthcare Web App 🏥

**GramArogya** is a modern web application aimed at improving access to affordable healthcare in rural areas. It offers appointment booking, symptom analysis using machine learning, and more to connect patients with nearby healthcare services effectively.

## 🌟 Features

- 📅 **Appointment Booking System** — Patients can book appointments online
- 🤖 **AI-based Symptom Checker** — Uses trained ML models to predict possible conditions
- 🗺️ **Location-based Doctor Discovery** *(planned)* — Integration with maps to find nearby doctors
- 🆘 **Emergency SOS Alert System** *(planned)* — One-click alert feature for emergencies
- 🎙️ **Voice Input Support** *(in progress)* — Hands-free form input using voice recognition
- 📈 **Analytics Dashboard** *(future)* — Admin dashboard for monitoring appointments and patient stats

## 📁 Project Structure

```bash
healthcare/
├── app.py                  # Main Flask app
├── train_model.py          # Model training script
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # Text vectorizer
├── appointments.csv        # Sample appointment data
├── create_db.py            # SQLite database creator
├── database.db             # Local SQLite DB
├── requirements.txt        # Python dependencies
├── static/                 # CSS, images
│   └── style.css
├── templates/              # HTML templates
│   ├── index.html
│   └── contact.html
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/healthcare.git
   cd healthcare
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python train_model.py
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

   <img width="1469" alt="Screenshot 2025-04-18 at 10 07 09 PM" src="https://github.com/user-attachments/assets/feb1c546-b2ed-4ccc-ba84-b65c3d02864d" />
   <img width="1466" alt="Screenshot 2025-04-18 at 10 10 45 PM" src="https://github.com/user-attachments/assets/07b3cc9f-dcf2-47a6-afbb-0b61ce35828f" />
   <img width="1458" alt="Screenshot 2025-04-18 at 10 11 55 PM" src="https://github.com/user-attachments/assets/5cb8298d-003e-4065-a42e-c8bab0f3675c" />
   <img width="1469" alt="Screenshot 2025-04-18 at 10 12 09 PM" src="https://github.com/user-attachments/assets/eebcf894-f481-40ae-b349-d6b018b84e66" />





## 🔍 Future Enhancements

- ✅ Add maps integration for locating nearby doctors
- ✅ Enable voice-assisted form inputs
- ✅ Implement emergency SOS button
- ✅ Add multilingual support
- ✅ Enhance UI with Bootstrap 5 components
- ✅ Deploy to Heroku or AWS


