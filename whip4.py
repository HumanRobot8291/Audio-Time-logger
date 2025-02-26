import whisper
import speech_recognition as sr
import time
import threading
from datetime import datetime

# Load Whisper model
model = whisper.load_model("base")

# File to store transcription
FILE_PATH = "transcription.txt"
RECORDING_TIME = 20  # Recording time in seconds

def countdown_timer():
    """Prints countdown every 2 seconds."""
    remaining_time = RECORDING_TIME
    while remaining_time > 0:
        print(f"Time remaining: {remaining_time} seconds...")
        time.sleep(2)
        remaining_time -= 2

def transcribe_speech():
    """Records speech for a fixed duration, transcribes it, and writes to a file."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening for {RECORDING_TIME} seconds...")
        
        # Start countdown timer thread
        countdown_thread = threading.Thread(target=countdown_timer)
        countdown_thread.start()

        # Listen for speech
        audio = recognizer.listen(source, timeout=RECORDING_TIME)
        
        # Wait for countdown thread to finish
        countdown_thread.join()

        # Save audio to a temp file
        temp_audio = "temp.wav"
        with open(temp_audio, "wb") as f:
            f.write(audio.get_wav_data())

        print("Processing speech...")

        # Transcribe using Whisper
        result = model.transcribe(temp_audio)
        text = result["text"].strip()

        # Append to text file
        with open(FILE_PATH, "a", encoding="utf-8") as file:
            file.write(f"{text} ({datetime.now()})\n")

        print(f"Saved: {text}")
        return text

def main():
    print("Voice recording started. Say something!")
    while True:
        # Start the transcribing in a separate thread
        listen_thread = threading.Thread(target=transcribe_speech)
        listen_thread.start()
        listen_thread.join()

        # Ask user if they want to continue
        choice = input("\nDo you want to record more? (y/n): ").strip().lower()
        if choice != "y":
            print("Exiting. Your transcriptions are saved in 'transcription.txt'.")
            break

if __name__ == "__main__":
    main()
