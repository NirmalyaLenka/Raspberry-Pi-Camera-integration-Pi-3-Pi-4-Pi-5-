# Raspberry Pi Camera Setup: Pi 3, Pi 4, and Pi 5

This repository documents the CSI camera connector differences between Raspberry Pi 3, Pi 4, and Pi 5, plus two small Python examples using Picamera2. The examples are standalone scripts in the repository root.

For current camera software documentation, see the [official Raspberry Pi camera documentation](https://www.raspberrypi.com/documentation/accessories/camera-software.html) and the [Picamera2 manual](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf).

## Board and cable differences

| Board | Camera connector | Practical note |
|---|---|---|
| Raspberry Pi 3 Model B/B+ | 15-pin CSI connector | Use a compatible camera ribbon cable and confirm its orientation for the board and module. |
| Raspberry Pi 4 Model B | 15-pin CSI connector | The connector size is compatible with the common Pi 3 cable format. |
| Raspberry Pi 5 | Smaller-pitch camera/display connectors | Use the correct Pi 5-compatible cable or adapter; a Pi 3/Pi 4 ribbon cable does not fit directly. |

The exact camera module, cable, Raspberry Pi OS release, and board revision affect compatibility. Power off the Pi before connecting or reseating the ribbon cable. Do not force the connector or guess the contact orientation; check the markings and the documentation for your board and camera module.

## Requirements

- Raspberry Pi 3, 4, or 5 running a supported Raspberry Pi OS release
- Compatible CSI camera module and the correct ribbon cable
- Network access for updates and package installation
- Terminal access locally or over SSH

Update the OS and reboot before debugging camera detection:

```bash
sudo apt update
sudo apt full-upgrade
sudo reboot
```

## Detect and test the camera

On Raspberry Pi OS Bookworm and later, the command-line camera applications use the `rpicam-*` names. Older OS releases may expose the earlier `libcamera-*` names.

List detected cameras:

```bash
rpicam-hello --list-cameras
```

Capture a still image:

```bash
rpicam-still --output test.jpg
```

Record a 10-second H.264 video:

```bash
rpicam-vid -t 10000 -o test.h264
```

These commands use the installed Raspberry Pi camera stack. If the camera is not listed, power down and check the cable, connector, module compatibility, OS update status, and the troubleshooting guide before changing configuration.

## Run the Python examples

The repository contains these scripts at the root; there is no `examples/` directory.

### Install Picamera2

Recent Raspberry Pi OS images may already include Picamera2. If it is missing, install the OS package:

```bash
sudo apt install -y python3-picamera2
```

Use the OS package rather than installing Picamera2 with `pip`, so it remains compatible with the system camera libraries. On a Lite installation, the official documentation also describes a no-recommends install option.

### Capture a photo

From the repository root:

```bash
python3 capture_photo.py
```

The script starts Picamera2, waits two seconds for exposure/white-balance adjustment, saves `photo.jpg` in the current directory, and stops the camera.

### Record a video

```bash
python3 record_video.py
```

The script records for 10 seconds with an H.264 encoder configured at 10,000,000 bits per second and writes `video.h264` in the current directory. Ensure enough free storage is available before recording.

These scripts are minimal examples, not a camera service or production recording application. They have not been run as part of this documentation review.

## Repository contents

| Path | Purpose |
|---|---|
| `README.md` | Board differences, setup, command-line checks, and Python instructions |
| `capture_photo.py` | Picamera2 still capture to `photo.jpg` |
| `record_video.py` | Picamera2 H.264 recording to `video.h264` |
| `camera-troubleshooting.md` | Camera detection and common error checks |

The current root tree does not contain a `LICENSE` file, a `requirements.txt`, or an `examples/` directory. Licensing terms are therefore not established by the current root files.

## Troubleshooting

See [camera-troubleshooting.md](camera-troubleshooting.md). Start by running `rpicam-hello --list-cameras` on a current Raspberry Pi OS release. If no camera is listed, solve detection and cabling first; Python script changes will not fix a camera that the system cannot see.

## Verification status

The README, both Python scripts, and the troubleshooting document were inspected. No camera was connected, no command-line capture was run, and neither Python script was executed or tested on a Raspberry Pi.

## Maintenance & Audit

- **Audit date:** 11 November 2026
- **Documentation status:** README aligned with the actual root-level scripts and current Raspberry Pi camera command names.
- **Verification boundary:** Documentation review only; no hardware or runtime result is claimed.
