# Camera Troubleshooting

Common camera-specific problems and how to fix them, across Pi 3, Pi 4, and Pi 5.

## "No cameras available" or Camera Not Detected

- Power off the Pi and reseat the ribbon cable, making sure it is pushed in fully and the locking clip is closed.
- Check the cable orientation. The metal contacts usually need to face toward the HDMI port on Pi 3/Pi 4 boards, though this can vary by camera module, so check your specific module's documentation.
- Confirm you are using the correct cable for your board. Pi 5 uses a different, smaller connector than Pi 3 and Pi 4, and needs its own cable or adapter.
- Run `sudo apt update && sudo apt full-upgrade` and reboot, since camera detection has improved across OS updates.
- Run `libcamera-hello --list-cameras` again after rebooting.

## Green or Purple Tinted Image

- This is often caused by a loose ribbon cable connection. Reseat the cable firmly.
- Confirm the camera module is fully compatible with your specific Pi model and OS version.

## Camera Preview Window Does Not Appear (but no error is shown)

- If you are connected over SSH without a desktop session, the preview window may not display. Use the `-o` flag to save output to a file instead of relying on the live preview.
- Try running the command directly on the Pi with a monitor connected instead of over SSH, if a live preview is required.

## "Failed to acquire camera" or Camera Busy Errors

- Make sure no other program (or a previous script that did not shut down cleanly) is still using the camera.
- Reboot the Pi to release any stuck camera resources.

## Picamera2 Import Errors in Python

- Confirm picamera2 is installed with:

```
sudo apt install -y python3-picamera2
```

- If you are using a Python virtual environment, picamera2 may need to be installed system-wide instead, since it depends on system libraries tied to `libcamera`.

## Old Tutorials Reference `raspistill` or `raspivid` and Nothing Works

- These tools belonged to the older legacy camera stack and have been replaced by `libcamera-still`, `libcamera-vid`, and the `picamera2` Python library on current Raspberry Pi OS releases.
- If you are following an older tutorial, look for the equivalent `libcamera-*` command instead.

## Still Stuck

Run `libcamera-hello --list-cameras` first to confirm the Pi can see the camera at all before troubleshooting further, since most issues trace back to detection rather than software configuration.
