import speech_recognition as sr
import pyttsx3
import time

def mock_accent_transfer(text, target_accent="british"):
    replacements = {
        "american": {"water": "wadder", "better": "bedder", "car": "cahr"},
        "british": {"water": "wah-tuh", "better": "beh-tuh", "car": "cah"},
        "indian": {"water": "vaa-ter", "better": "bettar", "car": "kaar"}
    }
    accent_map = replacements.get(target_accent.lower(), {})
    for word, alt in accent_map.items():
        text = text.replace(word, alt)
    return text

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)
        try:
            print("⏳ Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except sr.RequestError:
            print("❌ Could not connect to speech recognition service.")
    return ""

def main():
    print("🌐 GlobeTalk — Accent Converter Prototype")
    target_accent = input("Choose target accent (american/british/indian): ").strip().lower()
    
    while True:
        print("\n--- New Session ---")
        text = recognize_speech()
        if not text:
            continue

        converted_text = mock_accent_transfer(text, target_accent)
        print(f"🗣️ Accent Converted: {converted_text}")
        
        speak_text(converted_text)
        
        cont = input("Continue? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
