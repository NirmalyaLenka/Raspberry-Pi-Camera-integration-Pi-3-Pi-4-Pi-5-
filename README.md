# Raspberry Pi Camera Guide (Pi 3, Pi 4, Pi 5)

A beginner-friendly guide to setting up and using a camera module with the Raspberry Pi 3, Raspberry Pi 4, and Raspberry Pi 5. This covers hardware differences between the boards, wiring the camera correctly, enabling it in software, and running your first photo and video capture scripts.

## Board Specifications Relevant to the Camera

The camera connector and the software stack behind it changed across these three boards, so it helps to know the differences before you start.

### Raspberry Pi 3 Model B / B+

| Spec | Detail |
|---|---|
| SoC | Broadcom BCM2837B0 |
| CPU | Quad-core Arm Cortex-A53, 64-bit, 1.4 GHz |
| RAM | 1 GB LPDDR2 |
| Camera connector | Single 15-pin CSI camera port (standard size, same as Pi 1/2) |
| Display connector | Single DSI display port |
| USB | 4x USB 2.0 |
| Wireless | 2.4 GHz and 5 GHz 802.11ac, Bluetooth 4.2 |
| Power | 5V via micro-USB |
| Camera software stack | Works with the modern `libcamera`/`picamera2` stack on current Raspberry Pi OS; the older `raspistill`/`raspivid` tools are deprecated but may still exist on older OS images |

### Raspberry Pi 4 Model B

| Spec | Detail |
|---|---|
| SoC | Broadcom BCM2711 |
| CPU | Quad-core Arm Cortex-A72, 64-bit, 1.5 GHz (1.8 GHz on later revisions) |
| RAM | 1 / 2 / 4 / 8 GB LPDDR4 |
| Camera connector | Single 15-pin CSI camera port (standard size, same as Pi 3) |
| Display connector | Single DSI display port |
| USB | 2x USB 3.0, 2x USB 2.0 |
| Wireless | 2.4 GHz and 5 GHz 802.11ac, Bluetooth 5.0 |
| Power | 5V via USB-C |
| Camera software stack | `libcamera`/`picamera2`, the current default and recommended stack |

### Raspberry Pi 5

| Spec | Detail |
|---|---|
| SoC | Broadcom BCM2712 |
| CPU | Quad-core Arm Cortex-A76, 64-bit, 2.4 GHz |
| RAM | 2 / 4 / 8 / 16 GB LPDDR4X |
| GPU | VideoCore VII, with a redesigned image signal processor for improved camera performance |
| Camera connector | Two 4-lane MIPI camera/display connectors (smaller pitch than Pi 3/Pi 4 connectors), each usable as a camera or a display port, in any combination, supporting up to two cameras at once |
| USB | 2x USB 3.0, 2x USB 2.0 |
| Wireless | 2.4 GHz and 5 GHz 802.11ac, Bluetooth 5.0 |
| Power | 5V via USB-C, official 27W (5V 5A) supply recommended |
| Camera software stack | `libcamera`/`picamera2` only, this is the only supported stack |

Important cabling note: the Raspberry Pi 5 uses a different, smaller CSI connector than the Pi 3 and Pi 4. A camera ribbon cable made for Pi 3/Pi 4 will not directly fit a Pi 5. You need either a camera module that ships with the correct cable, or a separate adapter cable rated for the Pi 5's connector.

## What You Will Need

- A Raspberry Pi 3, 4, or 5 with Raspberry Pi OS installed and updated
- An official Raspberry Pi Camera Module (v1, v2, v3, or HQ Camera), or a compatible third-party CSI camera
- The correct CSI ribbon cable for your specific board (see the cabling note above)
- A monitor and keyboard, or an SSH connection to the Pi

## Step 1: Connect the Camera

1. Power off the Pi completely before connecting the camera.
2. Locate the CSI camera port. On Pi 3 and Pi 4 it is a single wide connector. On Pi 5 it is one of the two smaller connectors near the USB ports.
3. Gently pull up the plastic clip on the connector.
4. Insert the ribbon cable with the metal contacts facing the correct direction (usually facing the HDMI port on Pi 3/4, check your specific board's markings on Pi 5).
5. Push the plastic clip back down to lock the cable in place.
6. Power the Pi back on.

## Step 2: Update the System First

Camera support has changed significantly across Raspberry Pi OS versions, so update everything before testing:

```
sudo apt update
sudo apt full-upgrade
sudo reboot
```

## Step 3: Enable and Test the Camera

On current Raspberry Pi OS releases (Bullseye and later), the camera is generally detected automatically and uses the `libcamera` stack, with no manual enabling step required in most cases. If you are using an older OS image, you may still need to enable the legacy camera interface through:

```
sudo raspi-config
```

Under **Interface Options**, enable the camera if the option is present, then reboot.

To test that the camera is detected, run:

```
libcamera-hello --list-cameras
```

If your camera is recognized, you will see its name and supported resolutions listed.

## Step 4: Take a Test Photo

```
libcamera-still -o test.jpg
```

This opens a short preview, then saves a photo named `test.jpg` in your current folder.

## Step 5: Record a Test Video

```
libcamera-vid -t 10000 -o test.h264
```

This records a 10 second video (`-t` is in milliseconds) and saves it as `test.h264`.

## Step 6: Using the Camera with Python (Picamera2)

Picamera2 is the current official Python library for controlling the camera, and it works across Pi 3, Pi 4, and Pi 5.

Install it if it is not already present:

```
sudo apt install -y python3-picamera2
```

See `examples/capture_photo.py` and `examples/record_video.py` in this repository for ready-to-run scripts.

## Common Beginner Mistakes

- Connecting the ribbon cable backwards, or with contacts facing the wrong way
- Using a Pi 3/Pi 4 camera cable directly on a Pi 5 without an adapter
- Not fully seating the ribbon cable, causing a "camera not detected" error
- Forgetting to update the OS before testing, since older software may not detect newer camera modules correctly
- Touching the exposed ribbon cable contacts, which can introduce static damage

## Troubleshooting

See `docs/camera-troubleshooting.md` for a list of common camera-specific errors and fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.-integration-Pi-3-Pi-4-Pi-5-
