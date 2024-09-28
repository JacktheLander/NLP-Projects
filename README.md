Record.py tests the microphone to see if recording .wav is no issue.

Sampling.py records multiple chunks of audio continuously that could be sent to the server as they’re recorded.

Stitch.py rebuilds the chunks into a longer .wav file, which would be done on the server.

Transcribe.py sends the reconstructed .wav file from the server to google cloud and gets a transcription which is written to a text file.

Vosk works well and is not very compute demanding
