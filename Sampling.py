### Sampling.py continuously records in 5sec sound chunks to .wav

import sounddevice as sd
import numpy as np
import wave

# Parameters
sampling_rate = 44100  # 44.1kHz sample rate
duration = 5  # Duration of each recording in seconds
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


def continuous_recording():
    file_counter = 0  # Counter to generate unique filenames

    try:
        while True:
            # Create a unique filename for each 5-second chunk
            filename = f"output_audio_{file_counter}.wav"

            # Record audio and save it
            record_audio(filename)

            # Increment the file counter for the next recording
            file_counter += 1

    except KeyboardInterrupt:
        print("\nRecording stopped by user")


if __name__ == "__main__":
    continuous_recording()
