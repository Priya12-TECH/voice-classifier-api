from fastapi import FastAPI, Depends, HTTPException
from app.schemas import VoiceRequest, VoiceResponse
from app.auth import verify_api_key
from app.audio_utils import decode_audio, extract_features
from app.model import predict_voice

app = FastAPI()

SUPPORTED_LANGUAGES = ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]

@app.post("/api/voice-detection", response_model=VoiceResponse)
def voice_detection(payload: VoiceRequest, api_key: str = Depends(verify_api_key)):

    if payload.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail="Unsupported language")

    if payload.audioFormat.lower() != "mp3":
        raise HTTPException(status_code=400, detail="Only MP3 supported")

    signal, sr = decode_audio(payload.audioBase64)
    features = extract_features(signal, sr)

    classification, confidence = predict_voice(features)

    explanation = (
        "Unnatural pitch consistency detected"
        if classification == "AI_GENERATED"
        else "Natural pitch and speech variation observed"
    )

    return {
        "status": "success",
        "language": payload.language,
        "classification": classification,
        "confidenceScore": round(confidence, 2),
        "explanation": explanation
    }
