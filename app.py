
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    solar_data = {
        "plant_name": "SolarVision Plant",
        "location": "New Delhi, India",
        "current_power": "8.4 kW",
        "today_energy": "42.8 kWh",
        "battery": "87%",
        "grid": "Exporting",
        "weather": "Sunny ☀️",
        "temperature": "34°C",
        "co2_saved": "18.5 kg",
        "revenue": "₹320"
    }

    return render_template(
        "dashboard.html",
        data=solar_data
    )


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


if __name__ == "__main__":
    app.run(debug=True)
