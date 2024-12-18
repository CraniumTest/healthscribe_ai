from modules.transcription import MedicalTranscriber
from modules.recommendations import HealthRecommender
from modules.security import SecurityManager

def main():
    transcriber = MedicalTranscriber()
    recommender = HealthRecommender()
    security = SecurityManager()

    audio_file = 'path/to/audio/file.wav'
    transcription = transcriber.transcribe_audio(audio_file)
    print(f"Transcription: {transcription}")

    symptoms = "Patient reports a persistent cough and sore throat for three days."
    recommendation = recommender.generate_recommendation(symptoms)
    print(f"Recommendation: {recommendation}")

    encrypted_data = security.encrypt_data(transcription)
    print(f"Encrypted Transcription: {encrypted_data}")

    decrypted_data = security.decrypt_data(encrypted_data)
    print(f"Decrypted Transcription: {decrypted_data}")

if __name__ == '__main__':
    main()
