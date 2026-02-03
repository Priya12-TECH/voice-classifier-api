import base64
import requests

API_URL = "http://127.0.0.1:8000/api/voice-detection"
API_KEY = "sk_test_123456789"

# ✅ ONLY AUDIO FILE PATH
AUDIO_PATH = "samples/sample voice 2.mp3"

# Convert audio → Base64 (NO FILE SAVED)
with open(AUDIO_PATH, "rb") as audio_file:
    audio_base64 = base64.b64encode(audio_file.read()).decode("utf-8")

payload = {
    "language": "English",
    "audioFormat": "mp3",
    "audioBase64": audio_base64
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

response = requests.post(API_URL, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
