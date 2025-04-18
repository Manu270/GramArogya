# from flask import Flask, render_template, request, redirect
# import sqlite3

# app = Flask(__name__)

# # Home route
# @app.route("/")
# def index():
#     return render_template("index.html")

# # Appointment form
# @app.route("/book", methods=["GET", "POST"])
# def book():
#     if request.method == "POST":
#         name = request.form["name"]
#         village = request.form["village"]
#         contact = request.form["contact"]
#         reason = request.form["reason"]

#         conn = sqlite3.connect("database.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO appointments (name, village, contact, reason) VALUES (?, ?, ?, ?)",
#                        (name, village, contact, reason))
#         conn.commit()
#         conn.close()
#         return redirect("/")
#     return render_template("book.html")

# # Contact route
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# if __name__ == "__main__":
#     app.run(debug=True)


# 




# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/book')
# def book():
#     return render_template('book.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     symptoms = request.form['symptoms']
#     # Dummy prediction
#     prediction = "You might have a cold. Please consult a doctor."
#     return render_template('index.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)




# app.py

# from flask import Flask, render_template, request, redirect
# import sqlite3
# import pickle

# app = Flask(__name__)

# # Load trained model and vectorizer
# model = pickle.load(open("model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # Home page
# @app.route("/")
# def index():
#     return render_template("index.html")

# # Appointment booking
# @app.route("/book", methods=["GET", "POST"])
# def book():
#     if request.method == "POST":
#         name = request.form["name"]
#         village = request.form["village"]
#         contact = request.form["contact"]
#         reason = request.form["reason"]

#         try:
#             conn = sqlite3.connect("database.db")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO appointments (name, village, contact, reason) VALUES (?, ?, ?, ?)",
#                            (name, village, contact, reason))
#             conn.commit()
#             conn.close()
#             return redirect("/")
#         except Exception as e:
#             return f"Error saving to DB: {e}"

#     return render_template("book.html")

# # Contact page
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# # AI Symptom Predictor
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         symptoms = request.form["symptoms"]
#         symptoms_transformed = vectorizer.transform([symptoms])
#         prediction = model.predict(symptoms_transformed)[0]
#         return render_template("index.html", prediction=prediction)
#     except Exception as e:
#         return render_template("index.html", prediction="Error in prediction: " + str(e))

# if __name__ == "__main__":
#     app.run(debug=True)





#     now new

# app.py

from flask import Flask, render_template, request, redirect
import sqlite3
import pickle
import csv
import os

app = Flask(__name__)

# Load ML model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------- ROUTE: HOME ----------
@app.route("/")
def index():
    return render_template("index.html")

# ---------- ROUTE: APPOINTMENT BOOKING ----------
@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        # Get form values
        name = request.form["name"]
        village = request.form["village"]
        area = request.form["area"]
        contact = request.form["contact"]
        reason = request.form["reason"]
        time = request.form["time"]
        slot = request.form["slot"]

        try:
            # Save to database
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO appointments (name, village, contact, reason, area, time, slot)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (name, village, contact, reason, area, time, slot))
            conn.commit()
            conn.close()

            # Save to CSV file
            file_exists = os.path.isfile("appointments.csv")
            with open("appointments.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                if not file_exists:
                    writer.writerow(["Name", "Village", "Contact", "Reason", "Area", "Time", "Slot"])
                writer.writerow([name, village, contact, reason, area, time, slot])

            return render_template("book.html", success=True)
        except Exception as e:
            return f"Error saving to DB or CSV: {e}"

    return render_template("book.html", success=False)

# ---------- ROUTE: CONTACT PAGE ----------
@app.route("/contact")
def contact():
    return render_template("contact.html")

# ---------- ROUTE: AI SYMPTOM CHECKER ----------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        symptoms = request.form["symptoms"]
        symptoms_transformed = vectorizer.transform([symptoms])
        prediction = model.predict(symptoms_transformed)[0]
        return render_template("index.html", prediction=prediction)
    except Exception as e:
        return render_template("index.html", prediction="Error: " + str(e))

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
