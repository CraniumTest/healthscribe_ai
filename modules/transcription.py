import speech_recognition as sr
from transformers import pipeline

class MedicalTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.transcription_pipeline = pipeline('automatic-speech-recognition')

    def transcribe_audio(self, audio_file):
        try:
            with sr.AudioFile(audio_file) as source:
                audio_data = self.recognizer.record(source)
            transcription = self.transcription_pipeline(audio_data.get_wav_data(), return_text=True)
            return transcription['text']
        except Exception as e:
            print(f"Error in transcription: {e}")
            return None
