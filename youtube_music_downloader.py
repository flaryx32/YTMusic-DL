import yt_dlp
from ytmusicapi import YTMusic
from playsound import playsound
import os
import time

class YoutubeMusicDownloader:
    def __init__(self, ffmpeg_path=None, download_folder=None):
        self.ffmpeg_path = ffmpeg_path
        self.download_folder = download_folder or os.getcwd()
        self.ytmusic = YTMusic()

    def search_song(self, song_name):
        search_results = self.ytmusic.search(query=song_name, filter="songs")
        
        if not search_results:
            print("No results found!")
            return None
        
        most_relevant = search_results[0]
        title = most_relevant['title']
        artists = ", ".join([artist['name'] for artist in most_relevant['artists']])
        print(f"Automatically selected: {title} by {artists}")
        
        return most_relevant['videoId'], f"{title} by {artists}"

    def download_audio(self, video_id, filename):
        url = f"https://www.youtube.com/watch?v={video_id}"
        output_path = os.path.join(self.download_folder, f'{filename}.%(ext)s')
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'outtmpl': output_path,
        }
        
        if self.ffmpeg_path:
            ydl_opts['ffmpeg_location'] = self.ffmpeg_path

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading: {filename}")
                ydl.download([url])
            
            print(f"{filename} downloaded successfully as {filename}.wav!")
            return True
        except Exception as e:
            print(f"An error occurred while downloading: {str(e)}")
            return False

    def play_song(self, filename):
        file_path = os.path.join(self.download_folder, f"{filename}.wav")
        if os.path.exists(file_path):
            print(f"Playing {filename}.wav...")
            start_time = time.time()
            try:
                playsound(file_path)
                duration = time.time() - start_time
                minutes, seconds = divmod(int(duration), 60)
                print(f"\nSong finished. Duration: {minutes:02d}:{seconds:02d}")
            except Exception as e:
                print(f"An error occurred while playing the audio: {str(e)}")
        else:
            print("Downloaded song file not found.")

    def search_download_play(self, song_name):
        result = self.search_song(song_name)
        
        if result:
            video_id, formatted_filename = result
            if self.download_audio(video_id, formatted_filename):
                self.play_song(formatted_filename)

    def set_download_folder(self, folder_path):
        if os.path.isdir(folder_path):
            self.download_folder = folder_path
            print(f"Download folder set to: {folder_path}")
        else:
            print("Invalid folder path. Download folder not changed.")
