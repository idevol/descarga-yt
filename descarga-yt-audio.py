# importing packages
from pytube import YouTube
import ffmpeg
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# input YouTube URL
url_yt = input(f"{bcolors.OKGREEN}Ingresa la URL de YouTube:{bcolors.ENDC}\n>> ")

# Print loading message
print(f"{bcolors.OKCYAN}Descargando meta data, por favor espere{bcolors.ENDC}")

# url input from user
yt = YouTube(str(url_yt))

# extract only audio
video = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()

# check for destination to save file
print(f"{bcolors.OKGREEN}Ingresa la ruta de descarga (deja en blanco para que sea este mismo directorio):{bcolors.ENDC}")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'

convert_message = ''
if ext != '.mp3':
    # Print loading message
    print(f"{bcolors.OKCYAN}Convirtiendo en audio MP3, por favor espere{bcolors.ENDC}")

    # ffmpeg input webm audio file
    stream = ffmpeg.input(out_file)

    # ffmpeg output mp3
    stream = ffmpeg.output(stream, new_file)
    ffmpeg.run(stream, quiet=True)

    # delete audio file
    if os.path.isfile(out_file):
        os.remove(out_file)
    
    convert_message = ' y convertido en'

# result of success
print(yt.title + f"\n{bcolors.OKGREEN}Se ha descargado{convert_message} audio MP3.{bcolors.ENDC}")
