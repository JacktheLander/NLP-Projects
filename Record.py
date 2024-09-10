### Record.py is to setup a microphone input for recording a 5sec sound chunk to .wav

import sounddevice as sd
import numpy as np
import wave

# Parameters
sampling_rate = 44100  # 44.1kHz sample rate
duration = 5  # Duration of the recording in seconds
channels = 2  # Stereo


def record_audio(filename):
    print(f"Recording for {duration} seconds...")

    # Record the audio
    audio_data = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=channels, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save the audio data as a WAV file using the wave library
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit PCM format (2 bytes per sample)
        wf.setframerate(sampling_rate)
        wf.writeframes(audio_data.tobytes())

    print(f"Recording saved as {filename}")


if __name__ == "__main__":
    filename = "output_audio.wav"
    record_audio(filename)
