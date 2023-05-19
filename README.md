# mp3_to_wav
Python script that is able to convert a set of audio clips in MP3 format to WAV format.

To use this script, follow these steps:

Install the required dependencies by running the following command:
```
pip install pydub
```

Save the script in a file named mp3_to_wav_converter.py

Ensure that you have a folder containing the MP3 files you want to convert.

Open a command prompt or terminal and navigate to the directory wheremp3_to_wav_converter.py is located.

Run the script using the following command:
```
python mp3_to_wav_converter.py <mp3_folder> <output_folder>
```
Replace <mp3_folder> with the path to the folder containing the MP3 files, and <output_folder> with the path where you want to save the converted WAV files.

For example:
python mp3_to_wav_converter.py /path/to/mp3_folder /path/to/output_folder

The script will convert the MP3 files to WAV format and save them in the specified output folder. Progress and conversion details will be printed to the console.
