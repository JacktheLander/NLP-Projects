### Stitch.py concatenates .wav files to see how much recording is lost between saves
## 9/10 - While there is noticeable loss between files there is still enough data for transcription
# Note that longer chunks means less loss so test max sample duration to send to server

import wave
import os


def concatenate_wav_files(output_filename, input_filenames):
    """Concatenates multiple WAV files into one long WAV file."""

    # Open the first file to read its parameters (sample width, channels, frame rate)
    with wave.open(input_filenames[0], 'rb') as wf:
        params = wf.getparams()  # Get the parameters of the first file
        audio_data = [wf.readframes(wf.getnframes())]  # Start with the data from the first file

    # Iterate through the remaining files and append their data
    for filename in input_filenames[1:]:
        with wave.open(filename, 'rb') as wf:
            if wf.getparams() != params:
                raise ValueError("All WAV files must have the same parameters (sample rate, channels, etc.)")
            audio_data.append(wf.readframes(wf.getnframes()))  # Append the audio data

    # Write the concatenated audio data into a new output WAV file
    with wave.open(output_filename, 'wb') as wf_out:
        wf_out.setparams(params)  # Set the output file parameters to match the input files
        for data in audio_data:
            wf_out.writeframes(data)

    print(f"Concatenated audio saved as {output_filename}")


if __name__ == "__main__":
    # List of input WAV files to concatenate
    input_filenames = [
        "output_audio_0.wav",
        "output_audio_1.wav",
        "output_audio_2.wav"
    ]

    # Output filename for the concatenated result
    output_filename = "concatenated_output.wav"

    # Concatenate the WAV files
    concatenate_wav_files(output_filename, input_filenames)
