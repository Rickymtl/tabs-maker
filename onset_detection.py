from madmom.features.onsets import RNNOnsetProcessor, OnsetPeakPickingProcessor
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import librosa


def sample_audio(input_file, output_file, start_time, end_time):
    # sample the input audio file from start_time to end_time and saves the
    # segment to output_file
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Define start and end times for the segment (in milliseconds)
    start_time = start_time * 1000  # Convert to milliseconds
    end_time = end_time * 1000  # Convert to milliseconds

    # Slice the audio segment
    audio_segment = audio[start_time:end_time]

    # Save the audio segment as a new MP3 file
    audio_segment.export(output_file, format="wav")


def get_onsets_RNN(audio_file):
    proc = OnsetPeakPickingProcessor()
    onset_act = RNNOnsetProcessor()(audio_file)
    onsets = proc(onset_act)

    print(onsets)
    return onsets

def get_onset_superflux(audio_file):
    pass

def raw_spectrogram(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    # Compute the Short-Time Fourier Transform (STFT) to get the spectrogram
    S = np.abs(librosa.stft(y))#n_fft=16384//2, window="hamming", win_length=2048, hop_length=256))
    # Convert to decibel (dB) scale for better visualization
    S_db = librosa.amplitude_to_db(S, ref=np.max)
    return S_db, sr

def plot_spectrogram(S_db, sr, beat_times=[]):
    plt.figure(figsize=(10, 6))


    # Plot the dB-scaled spectrogram
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', cmap='magma')

    # Add a color bar and labels
    plt.colorbar(format='%+2.0f dB')
    plt.title('RNN onset detection')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

    # Show the plot
    plt.tight_layout()
    for beat in beat_times:
        plt.axvline(x=beat, color='cyan', linestyle='--', linewidth=1)

    # for note in notes_freqs:
    #     plt.axhline(y=note, color='yellow', linestyle='--', linewidth=1)
    plt.show()
if __name__ == '__main__':
    infile = "./../SCOM.mp3"
    outfile = "segment.wav"
    # sample_audio(infile, outfile, 0, 16)
    onsets = get_onsets_RNN(outfile)
    y, sr = raw_spectrogram(outfile)
    plot_spectrogram(y, sr, onsets)