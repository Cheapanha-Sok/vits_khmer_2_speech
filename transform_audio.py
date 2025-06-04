import os
import librosa
import soundfile as sf
import torchaudio.transforms as T
import torch

input_dir = 'dataset/wavs'
output_dir = 'clean_wav'
new_sr = 22050  # target sample rate

def do_resample(sr: int, new_sr: int):
    resampler = T.Resample(
        sr,
        new_sr,
        lowpass_filter_width=128,
        rolloff=0.99999,
        resampling_method="sinc_interp_hann",
    )
    return resampler

# ✅ Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.wav'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Load audio with its original sample rate
        y, sr = librosa.load(input_path, sr=None)

        # If it's not the target sample rate, resample it
        if sr != new_sr:
            print(f"Resampling {filename} from {sr} Hz to {new_sr} Hz")
            resampler = do_resample(sr, new_sr)
            y = resampler(torch.tensor(y)).numpy()
        else:
            print(f"{filename} already at {new_sr} Hz")

        # Save the audio to output directory
        sf.write(output_path, y, new_sr)

print("✅ All files processed.")
