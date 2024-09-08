# Youtube Music Downloader

This repository contains a Python script for downloading and playing audio from YouTube Music using the `yt-dlp` and `ytmusicapi` libraries. The program enables users to search for songs on YouTube Music, download the audio in `.wav` format, and play the audio locally.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Examples](#examples)
- [Installation](#installation)
- [Legal Disclaimer](#legal-disclaimer)
- [License](#license)

## Features
- **Song Search**: Search for songs on YouTube Music using the song's name.
- **Audio Download**: Download the audio in `.wav` format from the most relevant song result.
- **Audio Playback**: Play the downloaded `.wav` file using the `playsound` module.
- **Download Folder Customization**: Set a custom folder where downloaded audio files will be saved.
  
## Requirements
Before using this script, you need to install the following Python libraries:
- `yt-dlp`
- `ytmusicapi`
- `playsound`
- `ffmpeg`

You also need to have `ffmpeg` installed and accessible via your system's `PATH`. You can download `ffmpeg` from [here](https://ffmpeg.org/download.html).

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/flaryx32/YoutubeMusicDownloader.git
    cd YoutubeMusicDownloader
    ```

2. Install the required Python libraries:

    ```bash
    pip install yt-dlp ytmusicapi playsound
    ```

3. Download and install `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html).

4. Make sure the `ffmpeg` executable is available in your system's `PATH` or provide the path to it when initializing the class.

## Usage

1. Import the `YoutubeMusicDownloader` class:

    ```python
    from YoutubeMusicDownloader import YoutubeMusicDownloader
    ```

2. Initialize the downloader, optionally providing a path to `ffmpeg` and a download folder:

    ```python
    downloader = YoutubeMusicDownloader(ffmpeg_path='/path/to/ffmpeg', download_folder='/path/to/download/folder')
    ```

3. Use the `search_download_play` method to search for a song, download it, and play the audio:

    ```python
    downloader.search_download_play("Song Title")
    ```

4. Set a custom download folder if needed:

    ```python
    downloader.set_download_folder("/path/to/new/download/folder")
    ```

## Examples

### Example 1: Basic Song Search, Download, and Play
```python
downloader = YoutubeMusicDownloader()
downloader.search_download_play("Imagine by John Lennon")
```

### Example 2: Custom Download Folder
```python
downloader = YoutubeMusicDownloader()
downloader.set_download_folder("/Users/yourname/Music")
downloader.search_download_play("Bohemian Rhapsody by Queen")
```

### Example 3: Specifying a Custom FFmpeg Path
```python
downloader = YoutubeMusicDownloader(ffmpeg_path="/usr/local/bin/ffmpeg")
downloader.search_download_play("Shape of You by Ed Sheeran")
```

## Legal Disclaimer

This software is intended for **personal use only**. It is the user's responsibility to ensure that their usage of this program complies with all local laws and regulations, including those related to downloading copyrighted content.

Downloading audio from YouTube Music or any other platform may violate the platform's terms of service. This project is for educational purposes, and the author does not endorse any illegal use of this software.

## License

This code is released under a custom license that allows free private usage but **prohibits modifications, commercial usage, and redistribution** without explicit permission.

All rights to the code are owned by **@flaryx32**.

For contributions, please create a pull request. All changes should be tested locally before submitting.
