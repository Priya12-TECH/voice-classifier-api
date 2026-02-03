import base64
import librosa
import numpy as np
import io
import soundfile as sf

def decode_audio(base64_audio: str):
    audio_bytes = base64.b64decode(base64_audio)
    audio_buffer = io.BytesIO(audio_bytes)
    signal, sr = sf.read(audio_buffer)
    return signal, sr

def extract_features(signal, sr):
    mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)
    spectral_flatness = librosa.feature.spectral_flatness(y=signal)
    pitch = librosa.yin(signal, fmin=50, fmax=300)

    features = np.hstack([
        np.mean(mfcc, axis=1),
        np.mean(spectral_flatness),
        np.std(pitch)
    ])
    return features.reshape(1, -1)
