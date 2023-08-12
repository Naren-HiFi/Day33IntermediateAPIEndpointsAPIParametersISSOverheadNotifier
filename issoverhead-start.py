import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "infonaren55@gmail.com"
EMAIL_PASSWORD = "uyeimfunxtpufhna"
TO_MAIL_ADDRESS = "narenbagavathye5@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    lat_position = iss_latitude
    lng_position = iss_longitude
    if MY_LAT - 5 <= lat_position <= MY_LAT + 5 and MY_LONG - 5 <= lng_position <= MY_LONG + 5:
        return True
    else:
        return False
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_MAIL_ADDRESS,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )




