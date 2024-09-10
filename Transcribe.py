### Transcribe would be run from our servers. This is using google cloud but could use other services that can be downloaded
### Works well with 5sec samples the loss imbetween stitching does not affect transcription

import os
import io
from google.cloud import speech
from pydub import AudioSegment

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Jack Landers\PycharmProjects\SpeechRecognition\GCP_creds.json'

def convert_to_mono(input_file, output_file):
    # Load the stereo audio file
    audio = AudioSegment.from_wav(input_file)

    # Convert it to mono
    mono_audio = audio.set_channels(1)

    # Export the mono audio to a new file
    mono_audio.export(output_file, format="wav")
    print(f"Converted {input_file} to mono. Saved as {output_file}")
def transcribe_audio(file_path, output_text_file):
    # Initialize a SpeechClient
    client = speech.SpeechClient()

    # Load the audio file into memory
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    # Configure audio and recognition parameters
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,  # Adjust based on your WAV file's sample rate
        language_code="en-US",    # Adjust to your language code
    )

    # Transcribe the audio using Google Cloud API
    response = client.recognize(config=config, audio=audio)

    # Collect transcription
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript + "\n"

    # Save the transcription to a text file
    with open(output_text_file, "w") as text_file:
        text_file.write(transcription)
    print(f"Transcription saved to {output_text_file}")

if __name__ == "__main__":
    # Path to your input stereo WAV file and output mono WAV file
    input_file = "concatenated_output.wav"
    mono_file = "mono_output.wav"
    # Output text file for saving the transcription
    output_text_file = "transcription.txt"

    # Convert stereo to mono
    convert_to_mono(input_file, mono_file)

    # Check if GOOGLE_APPLICATION_CREDENTIALS is set
    if os.getenv('GOOGLE_APPLICATION_CREDENTIALS') is None:
        print("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")
        print("Please set it to the path of your Google Cloud service account JSON key.")
    else:
        # Transcribe the audio file
        transcribe_audio(mono_file, output_text_file)
