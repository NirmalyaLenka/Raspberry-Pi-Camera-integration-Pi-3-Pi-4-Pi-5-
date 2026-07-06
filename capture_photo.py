"""
Basic photo capture example using Picamera2.

Works on Raspberry Pi 3, Pi 4, and Pi 5, as long as picamera2 is
installed and a camera module is properly connected.

Install picamera2 first if needed:
    sudo apt install -y python3-picamera2

Run with:
    python3 capture_photo.py
"""

from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()

# Use a still-image optimized configuration
config = picam2.create_still_configuration()
picam2.configure(config)

picam2.start()

# Give the sensor a moment to adjust exposure and white balance
sleep(2)

picam2.capture_file("photo.jpg")
print("Saved photo.jpg")

picam2.stop()
