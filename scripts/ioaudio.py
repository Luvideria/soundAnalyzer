import pyaudio
import wave
def sigToWav(data, stream, out):
    waveFile = wave.open(out, 'wb')
    waveFile.setnchannels(stream._channels)
    waveFile.setsampwidth(pyaudio.get_sample_size(stream._format))
    waveFile.setframerate(stream._rate)
    waveFile.writeframes(b''.join(data))
    waveFile.close()