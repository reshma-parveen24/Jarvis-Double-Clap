# JARVIS Double Clap Workspace Trigger

A Python-based JARVIS workspace trigger that detects a **double clap** using the microphone and automatically opens a YouTube channel in Google Chrome.

## ✨ Features

- 🎙️ Real-time microphone listening
- 👏 Clap detection using audio amplitude
- 👏👏 Double-clap recognition
- 🌐 Automatically opens YouTube in Google Chrome
- 💻 Supports Windows, macOS, and Linux

## 🛠️ Technologies Used

- Python
- PyAudio
- NumPy

## 📁 Project Structure

```text
Jarvis-Double-Clap/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
Requirements
Python 3.9+
A working microphone
Google Chrome
PyAudio
NumPy
🚀 Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Jarvis-Double-Clap.git
cd Jarvis-Double-Clap
2. Create a virtual environment
Windows
python -m venv .venv
.venv\Scripts\activate
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
▶️ Run the Project

Start the program with:

python app.py

You should see:

Listening for double claps... (Press Ctrl+C to stop)

Now make two claps within the configured time interval.

When a double clap is detected, the program will open the configured YouTube channel in Google Chrome.

🔧 Configuration

The clap detection settings can be changed in app.py:

THRESHOLD = 3000
MIN_DELAY = 0.2
MAX_DELAY = 1.0
THRESHOLD

Controls how loud a sound needs to be to register as a clap.

A higher value makes detection less sensitive.

MIN_DELAY

The minimum time between two detected claps.

This helps prevent echoes or the same clap from being detected twice.

MAX_DELAY

The maximum amount of time allowed between the first and second clap.

If the second clap occurs after this time, the counter resets.

🔄 How It Works
The program starts listening to the microphone.
Audio is captured continuously using PyAudio.
NumPy checks the peak audio level.
A sound above the threshold is considered a clap.
The program checks the time between detected claps.
Two valid claps within the allowed time trigger the workspace protocol.
Google Chrome opens the configured YouTube channel.
The microphone pauses temporarily to prevent unwanted triggers.
🌐 YouTube URL

The project can use a custom YouTube URL through the YOUTUBE_URL environment variable.

Example:

YOUTUBE_URL=https://youtube.com/@your_channel

If no custom URL is provided, the default URL configured in app.py is used.

🖥️ Platform Support

The project includes support for:

Windows
macOS
Linux

If Chrome cannot be opened directly, the program falls back to the system's default browser.

🛑 Stop the Program

Press:

Ctrl+C

The program will safely close the microphone stream and shut down the audio system.

⚠️ Troubleshooting
Claps are not detected

Try lowering the threshold:

THRESHOLD = 2000
Too many false detections

Try increasing the threshold:

THRESHOLD = 4000

You can also increase MIN_DELAY to reduce duplicate detections.

PyAudio installation fails

Try upgrading pip:

python -m pip install --upgrade pip

Then install the requirements again:

pip install -r requirements.txt

PyAudio may require additional system audio dependencies depending on your operating system.

🚀 Future Improvements
🎤 Voice commands
🖥️ GUI interface
⚡ More workspace automation
👏 Multiple clap patterns
🔊 Sound notifications
⚙️ Customizable actions
🧠 Improved noise filtering
