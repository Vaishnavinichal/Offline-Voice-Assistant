# Offline Voice Assistant

## Overview
This project is an **offline voice assistant** built using **OpenAI Whisper** for speech recognition.  
It supports **multilingual speech (English and Marathi)** and responds using **text-to-speech**, without requiring an internet connection.

The goal of this project is to demonstrate how **speech recognition can be integrated into a real application**, while handling practical challenges such as audio quality, recognition accuracy, and system performance.

---

##  System Architecture

User Speech  
→ Microphone Recording  
→ Audio Normalization  
→ Whisper ASR (Speech → Text)  
→ Text Processing  
→ Text-to-Speech Response (spoken echo of recognized text)


---

## Technologies Used
- Python  
- OpenAI Whisper (offline ASR)  
- sounddevice & soundfile (audio recording)  
- pyttsx3 (text-to-speech)  

---

## Features
- Fully **offline voice assistant**
- Supports **English and Marathi speech**
- Push-to-talk interaction model
- Converts spoken input into text using Whisper
- Speaks back the recognized text
- Handles microphone audio normalization for better accuracy

---

## Design Decisions
- **Offline ASR** was chosen to avoid dependency on cloud APIs
- **Push-to-talk** interaction was used instead of wake-word detection to improve accuracy and reduce CPU load
- **Audio normalization** was added to handle low microphone input levels
- Whisper multilingual model was selected to support Indian languages

---

## Limitations
- Not designed for continuous background listening
- Accuracy depends on microphone quality and environment noise
- Offline inference introduces noticeable latency on CPU
- Not suitable for singing or chanting audio

---

## Learning Outcomes
- Understanding real-world speech recognition pipelines
- Handling microphone audio issues such as low gain
- Working with offline ASR models
- Designing voice-based systems with practical constraints
- Applying engineering trade-offs between accuracy and performance

---

## Future Improvements
- NLP-based intent detection instead of direct text responses
- Phonetic or fuzzy matching for improved robustness
- Support for additional Indian languages
- GUI-based interaction

---

## How to Run

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies  
   pip install -r requirements.txt
