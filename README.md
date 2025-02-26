# Audio-Time-logger
It records what you say in a notebook that you can use later to update your timesheet/log for work. Speech to Text set up.

# Prerequisites: 
You need python installed.

# To set up the program use the following steps.
# Speech Transcription Setup Guide

## Prerequisites
Ensure you have Python installed (version 3.8 or higher is recommended). You can check your Python version using:

```bash
python --version
```

## Installation
Install the necessary dependencies by running:

```bash
pip install openai-whisper SpeechRecognition torch numpy
```

Additionally, install FFmpeg, which is required for Whisper to process audio files. You can install it using:

### Windows:
Download and install FFmpeg from [FFmpeg official site](https://ffmpeg.org/download.html). Ensure FFmpeg is added to the system PATH.

### macOS (Homebrew):
```bash
brew install ffmpeg
```

### Linux (Debian/Ubuntu):
```bash
sudo apt update && sudo apt install ffmpeg
```

## Running the Script
Save the script as `transcribe.py` and run it with:

```bash
python transcribe.py
```

The script will:
1. Load the Whisper model.
2. Start recording from the microphone for 20 seconds.
3. Transcribe the recorded speech using Whisper.
4. Append the transcribed text to `transcription.txt`.
5. Prompt the user to continue or exit.

## Output File
All transcriptions are saved in `transcription.txt` with timestamps.

## Notes
- Ensure your microphone is properly configured.
- For longer recordings, modify `RECORDING_TIME` in the script.
- If Whisper runs slowly, consider using a smaller model (`tiny` or `small`) instead of `base`.
- If you encounter errors, verify that FFmpeg is installed correctly by running:
  ```bash
  ffmpeg -version
  ```

