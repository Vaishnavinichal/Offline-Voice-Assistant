import whisper
import sounddevice as sd
import soundfile as sf
import pyttsx3
import datetime
import os
import webbrowser

# ---------------- CONFIG ----------------
SAMPLE_RATE = 16000
DURATION = 8                  # longer audio = better accuracy
AUDIO_FILE = "command.wav"

# Use SMALL model for better Indian language accuracy
model = whisper.load_model("small")
engine = pyttsx3.init()

# ---------------- SPEAK ----------------
def speak(text):
    print("ASSISTANT:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- RECORD ----------------
def record_audio():
    print("Speak now...")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    sf.write(AUDIO_FILE, audio, SAMPLE_RATE)

# ---------------- TRANSCRIBE ----------------
def transcribe_audio():
    print("Processing speech...")
    result = model.transcribe(AUDIO_FILE, fp16=False)
    text = result["text"].strip().lower()
    language = result["language"]

    print("Detected language:", language)
    print("You said:", text)

    return text

# ---------------- INTENT HANDLING ----------------
def handle_command(text):
    # TIME
    if any(word in text for word in ["time", "वेळ"]):
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # GOOGLE
    elif any(word in text for word in ["google", "गुगल", "browser"]):
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # FOLDER
    elif any(word in text for word in ["folder", "फोल्डर"]):
        speak("Opening folder")
        os.startfile(os.getcwd())

    # EXIT
    elif any(word in text for word in ["exit", "stop", "थांब"]):
        speak("Goodbye")
        exit(0)

    # UNKNOWN
    else:
        speak("Sorry, I could not understand the command clearly")

# ---------------- MAIN ----------------
def main():
    speak("Offline voice assistant ready")

    while True:
        input("\nPress ENTER to speak...")
        record_audio()
        command_text = transcribe_audio()
        handle_command(command_text)

if __name__ == "__main__":
    main()
