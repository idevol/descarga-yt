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
print(f"{bcolors.OKCYAN}Descargando lista de vieos disponibles, por favor espere{bcolors.ENDC}")

# url input from user
yt = YouTube(str(url_yt), use_oauth=True, allow_oauth_cache=True)

# videos disponibles
videos = yt.streams.filter(type='video').order_by('resolution').desc()

for idx, video_element in enumerate(videos):
    list_num = idx + 1
    space = " " if list_num < 10 else ""
    print(f"{space}{list_num}) resolución: {video_element.resolution}\tFPS:{video_element.fps}\tmime type:{video_element.mime_type}\tcodec:{video_element.video_codec}")

video_num = int(str(input(f"{bcolors.OKGREEN}Ingresa el número del video a descargar (deja en blanco para que sea el 1):{bcolors.ENDC}\n>> ")) or 1)

# select video
video = videos[video_num - 1]

# check for destination to save file
print(f"{bcolors.OKGREEN}Ingresa la ruta de descarga (deja en blanco para que sea este mismo directorio):{bcolors.ENDC}")
destination = str(input(">> ")) or '.'

# Print loading message
print(f"{bcolors.OKCYAN}Descargando el video selecionado, por favor espere{bcolors.ENDC}")

# download the file
out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)

convert_message = ''

if ext != '.mp4':
    convert = str(input(f"{bcolors.OKGREEN}¿Convertir a MP4? (deja en blanco para no):{bcolors.ENDC}\n>> ")) or 'no'
    if convert != 'no':
        # Print loading message
        print(f"{bcolors.OKCYAN}Convirtiendo video a MP4{bcolors.ENDC}")

        # ffmpeg input webm audio file
        stream = ffmpeg.input(out_file)
        new_file = base + '.mp4'
        
        # ffmpeg output mp3
        stream = ffmpeg.output(stream, new_file)
        ffmpeg.run(stream, quiet=True)

        # delete video file
        if os.path.isfile(out_file):
            os.remove(out_file)
        
        convert_message = ' y convertido a MP4'

# result of success
print(yt.title, f"\n{bcolors.OKGREEN}Se ha descargado el video{convert_message}.{bcolors.ENDC}")
