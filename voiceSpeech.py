from google.cloud import texttospeech
import os

# Créer une instance du client TTS
client = texttospeech.TextToSpeechClient()


# Configurer la synthèse vocale
voice = texttospeech.VoiceSelectionParams(

language_code="fr-FR", # langage utilisé
name="fr-FR-Wavenet-D" # type de voix

)

audio_config = texttospeech.AudioConfig(
audio_encoding=texttospeech.AudioEncoding.MP3 # format de sortie

)


# Récupérer le texte à synthétiser
texte = "Votre annotation à lire à haute voix"

# Générer la requête pour synthétiser la voix
synthesis_input = texttospeech.SynthesisInput(text=texte)

# Appeler l'API pour synthétiser la voix
response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# Enregistrer le fichier audio généré
with open('annotation.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "annotation.mp3"')


# Jouer le fichier audio
os.system("start annotation.mp3")





