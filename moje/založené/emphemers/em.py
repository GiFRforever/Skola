import platform
from skyfield.api import load, wgs84
from datetime import datetime, timedelta

# Load the ephemeris data for the planets and stars
planets = load("de421.bsp")
# stars = load("bright_stars_novas_de418.bsp")

# Get the current location of the user based on the platform
if platform.system() == "Windows":
    import geocoder

    # Get the user's location based on their IP address
    location = geocoder.ip("me")

    latitude = location.lat
    longitude = location.lng
    observer = wgs84.latlon(latitude, longitude)
elif platform.system() == "Android":
    import android
    from android.permissions import Permission, request_permissions

    # Request location permission from the user
    request_permissions(
        [Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION]
    )
    droid = android.Android()

    # Get the current location of the user
    location = droid.readLocation().result
    latitude = location["network"]["latitude"]
    longitude = location["network"]["longitude"]
    observer = wgs84.latlon(latitude, longitude)
else:
    print("Unsupported platform.")
    exit()

# Ask the user for the time, default to the current time
input_time = input(
    "Enter time in the format 'YYYY-MM-DD HH:MM:SS', or leave blank for current time: "
)
if input_time:
    dt = datetime.strptime(input_time, "%Y-%m-%d %H:%M:%S")
else:
    dt = datetime.utcnow()

# Get the list of available celestial bodies
body_list = list(planets.keys())  # + list(stars.keys())

# Ask the user for the choice of celestial body
choice = input(
    "Enter the name of the celestial body you want to calculate the position for, or type 'list' to see available options: "
)
while choice.lower() == "list":
    print("Available celestial bodies:")
    for body_name in body_list:
        print(f"- {body_name}")
    choice = input(
        "Enter the name of the celestial body you want to calculate the position for, or type 'list' to see available options: "
    )

# Check if the user's choice is valid
if choice.lower() == "sun":
    body = planets["sun"]
elif choice.lower() == "moon":
    body = planets["moon"]
elif choice.lower() in planets:
    body = planets[choice.lower()]
# elif choice.lower() in stars:
#     body = stars[choice.lower()]
else:
    print("Invalid choice.")
    exit()

# Get the position of the celestial body at the specified time
ts = load.timescale()
t = ts.utc(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
position = observer.at(t).observe(body).apparent()

# Print the position of the celestial body
alt, az, distance = position.altaz()
print(f"At {dt} the {choice} is at altitude {alt} and azimuth {az} from your location.")
