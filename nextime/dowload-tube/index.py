import os
import yt_dlp

# Define o caminho do ffmpeg para o ambiente do Jupyter
os.environ["FFMPEG_BINARY"] = "/opt/homebrew/bin/ffmpeg"
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

def download_videos(urls: list[str], output_path: str = "."):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Baixa a melhor qualidade disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Define o nome do arquivo de saída
        'merge_output_format': 'mp4'  # Formato final do vídeo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

# Lista de URLs dos vídeos
video_urls = [
    "https://www.youtube.com/watch?v=xKDzG6cSOyk",
    "https://www.youtube.com/watch?v=44C7Gfjt-mI&t=1s",
    "https://www.youtube.com/watch?v=EPDt9j2F86U",
    "https://www.youtube.com/watch?v=ZIqxDzFjOxA"
]

# Chama a função para baixar os vídeos
download_videos(video_urls)
