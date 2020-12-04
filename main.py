import requests
import smtplib

my_api = "apigoeshere"
MY_LAT = 43.129178
MY_LONG = -79.213106
my_email = "email"
my_password = "pass"
EXCLUDES = "current,minutely,daily,alerts"
will_rain = False

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&exclude={EXCLUDES}&units=metric&appid={my_api}")
response.raise_for_status()
weather_data = response.json()
hourly_weather_codes = [weather_data["hourly"][code]["weather"][0]["id"] for code in range(12)]


def send_email(to="", text=""):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to,
                            msg=f"Subject: Weather Alert\n\n{text}")


for i in hourly_weather_codes:
    if i < 700:
        will_rain = True
        send_email(to="email", text="Pack an umbrella, it will rain today.")
        break


