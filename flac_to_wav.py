import os
import subprocess

# Get a list of all FLAC files in the current directory
flac_files = [file for file in os.listdir() if file.lower().endswith('.flac')]

if len(flac_files) == 0:
    print("No FLAC files found in the current directory.")
    exit()

# Create a list of input arguments for ffmpeg
input_args = []
for i, file in enumerate(flac_files):
    input_args.extend(['-i', file])

# Build the filter_complex argument
filter_args = ''.join([f'[{i}:0]' for i in range(len(flac_files))])
filter_complex = f'{filter_args}concat=n={len(flac_files)}:v=0:a=1[out]'

# Set the output file name
output_file = 'output.wav'

# Build the ffmpeg command
ffmpeg_command = ['ffmpeg']
ffmpeg_command.extend(input_args)
ffmpeg_command.extend(['-filter_complex', filter_complex])
ffmpeg_command.extend(['-map', '[out]', output_file])

# Execute the ffmpeg command
subprocess.call(ffmpeg_command)

print("FLAC files joined and saved as WAV file:", output_file)
