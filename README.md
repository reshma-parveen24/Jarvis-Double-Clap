# JARVIS Double Clap Workspace Trigger

A Python-based JARVIS workspace trigger that detects a **double clap** using the microphone and automatically opens a YouTube channel in Google Chrome.

## ✨ Features

* 🎙️ Real-time microphone listening
* 👏 Clap detection using audio amplitude
* 👏👏 Double-clap recognition
* 🌐 Automatically opens YouTube in Google Chrome
* 💻 Supports Windows, macOS, and Linux

## 🛠️ Technologies Used

* Python
* PyAudio
* NumPy

## 📁 Project Structure

```text
Jarvis-Double-Clap/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
```

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.9+
* A working microphone
* Google Chrome
* PyAudio
* NumPy

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/reshma-parveen24/Jarvis-Double-Clap.git
cd Jarvis-Double-Clap
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

Start the program with:

```bash
python app.py
```

You should see:

```text
Listening for double claps... (Press Ctrl+C to stop)
```

Now make **two claps within the configured time interval**.

When a double clap is detected, the program will open the configured YouTube channel in Google Chrome.

## 🔧 Configuration

The clap detection settings can be changed in `app.py`:

```python
THRESHOLD = 3000
MIN_DELAY = 0.2
MAX_DELAY = 1.0
```

### `THRESHOLD`

Controls how loud a sound needs to be to register as a clap.

If your claps are not being detected, try lowering the value.

If the program detects too much background noise, try increasing the value.

### `MIN_DELAY`

The minimum time between two detected claps.

This helps prevent echoes or the same clap from being detected twice.

### `MAX_DELAY`

The maximum amount of time allowed between the first and second clap.

If the second clap occurs after this time, the clap counter resets.

## 🔄 How It Works

1. The program starts listening to the microphone.
2. Audio is captured continuously using PyAudio.
3. NumPy calculates the peak audio level.
4. A sound above the threshold is considered a clap.
5. The program checks the time between detected claps.
6. Two valid claps within the allowed time trigger the workspace protocol.
7. Google Chrome opens the configured YouTube channel.
8. The microphone pauses temporarily to help prevent unwanted triggers.

## 🌐 YouTube URL

The project contains a configurable YouTube URL.

The default URL is defined in `app.py`.

You can also override it by setting the `YOUTUBE_URL` environment variable.

### Windows

```bash
set YOUTUBE_URL=https://youtube.com/@your_channel
python app.py
```

### macOS / Linux

```bash
export YOUTUBE_URL=https://youtube.com/@your_channel
python app.py
```

The `.env.example` file is included as a template for the YouTube URL configuration.

## 🖥️ Platform Support

The project includes Chrome-opening logic for:

* Windows
* macOS
* Linux

If Chrome cannot be opened directly, the program falls back to the system's default browser.

## 🛑 Stop the Program

To stop the program, press:

```text
Ctrl+C
```

The application will safely close the microphone stream and shut down the audio system.

## ⚠️ Troubleshooting

### Claps are not detected

Try lowering the threshold:

```python
THRESHOLD = 2000
```

### Too many false detections

Try increasing the threshold:

```python
THRESHOLD = 4000
```

You can also increase `MIN_DELAY` to reduce duplicate detections.

### PyAudio installation fails

First, upgrade pip:

```bash
python -m pip install --upgrade pip
```

Then try installing the dependencies again:

```bash
pip install -r requirements.txt
```

> PyAudio may require additional system-level audio dependencies depending on your operating system.

### Chrome does not open

Make sure Google Chrome is installed on your computer.

The application also attempts to fall back to the default browser if Chrome cannot be opened directly.

## 🚀 Future Improvements

* 🎤 Voice commands
* 🖥️ Graphical user interface
* ⚡ More workspace automation
* 👏 Multiple clap patterns
* 🔊 Sound notifications
* ⚙️ Customizable actions
* 🧠 Improved noise filtering
* 🎯 More accurate clap detection

## 👩‍💻 Author

**Reshma Parveen**


