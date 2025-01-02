import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 19.751480 # Your latitude
MY_LONG = 75.713890 # Your longitude

def iss_is_overhead ():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <=iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <=iss_longitude <= MY_LONG:
        return True

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def it_is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour < sunrise:
        return True


while True:
    time.sleep(60)
    if iss_is_overhead() and it_is_dark():
        MY_EMAIL = "josephtelng2004gmail.com"
        PASSWORD = "cqru rngj vqzw yogd"
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs="josephtelang30@Yahoo.com",msg="subject:Look up \n\n The ISS is above you in the sky.")
        

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



