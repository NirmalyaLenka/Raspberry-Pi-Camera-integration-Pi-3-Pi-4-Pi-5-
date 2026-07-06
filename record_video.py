"""
Basic video recording example using Picamera2.

Works on Raspberry Pi 3, Pi 4, and Pi 5, as long as picamera2 is
installed and a camera module is properly connected.

Install picamera2 first if needed:
    sudo apt install -y python3-picamera2

Run with:
    python3 record_video.py
"""

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from time import sleep

picam2 = Picamera2()

# Use a video-optimized configuration
config = picam2.create_video_configuration()
picam2.configure(config)

encoder = H264Encoder(bitrate=10000000)

picam2.start_recording(encoder, "video.h264")
print("Recording for 10 seconds...")
sleep(10)
picam2.stop_recording()

print("Saved video.h264")
