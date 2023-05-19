import os
import sys
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of MP3 files in the input folder
    mp3_files = [file for file in os.listdir(mp3_folder) if file.lower().endswith('.mp3')]

    # Convert each MP3 file to WAV format
    for mp3_file in mp3_files:
        mp3_path = os.path.join(mp3_folder, mp3_file)
        wav_file = os.path.splitext(mp3_file)[0] + '.wav'
        wav_path = os.path.join(output_folder, wav_file)

        # Load the MP3 file
        audio = AudioSegment.from_mp3(mp3_path)

        # Export the audio to WAV format
        audio.export(wav_path, format='wav')

        print(f"Converted {mp3_file} to {wav_file}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Please provide two arguments: MP3 folder and output folder.")
        print("Example: python audio_converter.py mp3_folder output_folder")
        sys.exit(1)

    # Get the command-line arguments
    mp3_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Convert MP3 files to WAV format
    convert_mp3_to_wav(mp3_folder, output_folder)
