import pyaudio
import numpy as np
import time
import os
import platform
import subprocess

THRESHOLD = 3000  # How loud a sound needs to be to register as a "clap". Adjust if it's too sensitive or not sensitive enough.
MIN_DELAY = 0.2  # Minimum seconds between claps to avoid echoing registering as a second clap.
MAX_DELAY = 1.0  # Maximum seconds between claps. If you wait longer, it resets.

CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

YOUTUBE_URL = "https://youtube.com/@reshmaparveen_24?si=TxmSXlXmmKGSKwwg"


def open_chrome(url):
    """Open a URL in Google Chrome, cross-platform."""
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.Popen(["start", "chrome", url], shell=True)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", "-a", "Google Chrome", url])
        else:  # Linux
            subprocess.run(["google-chrome", url])
    except Exception as e:
        print(f"Couldn't open Chrome directly ({e}), falling back to default browser...")
        import webbrowser
        webbrowser.open(url)


p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening for double claps... (Press Ctrl+C to stop)")

last_clap_time = 0
clap_count = 0

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)

        peak = np.abs(audio_data).max()

        if peak > THRESHOLD:
            current_time = time.time()
            time_since_last_clap = current_time - last_clap_time

            if time_since_last_clap > MIN_DELAY:
                if time_since_last_clap < MAX_DELAY:
                    clap_count += 1
                else:
                    clap_count = 1

                last_clap_time = current_time
                print(f"Clap detected! (Count: {clap_count})")

                if clap_count == 2:
                    print("Double clap confirmed! Initiating Workspace Protocol...")

                    # Add Tasks Here

                    time.sleep(2)

                    # Opening Chrome to directly open my YouTube channel
                    open_chrome(YOUTUBE_URL)

                    clap_count = 0

                    print("Workspace active. Pausing JARVIS microphone so music doesn't trigger it...")

                    time.sleep(14400)

except KeyboardInterrupt:
    print("\nShutting down JARVIS audio system...")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()