# TunesToMP4 - A Free and Safe Alternative to TunesToTube

TunesToMP4 is a simple and safe Python-based tool that allows you to create videos with a still image and an audio track. Unlike TunesToTube, this tool can be self-hosted, runs on your own computer, and is completely free, ensuring your data privacy and security.

## Features

- Combine an image and an audio file (MP3/WAV) into a single video file (MP4).
- Maintain the aspect ratio of the image or stretch it to fit the output resolution.
- Add a customizable watermark to the output video.
- Easy-to-use GUI for selecting image, audio, and output options.

## Getting Started

### Prerequisites

- Python 3.6 or newer
- MoviePy
- Pillow (PIL)

### Installation

1. Clone the repository:

```
git clone https://github.com/pvpb0t/tunetotube.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Download the ImageMagick installer from the official website: https://imagemagick.org/script/download.php
4. Run the installer and make sure to check the "Install legacy utilities" option during the installation process. This is important for compatibility with MoviePy.
Here is a screenshot of the option to check during installation:
![bild](https://user-images.githubusercontent.com/74259011/235322866-759c4699-4d2c-48d4-9285-dc9d6f3eb2df.png)

After installing ImageMagick, restart your Python script or application.


### Usage

1. Run the GUI-based desktop application:

```
python main.py
```
The application will open a window where you can browse for an image and audio file, select the stretch image option, and create a video. The final output video will be saved as "output.mp4" in the same directory as the script.

## Benefits over TunesToTube

- No need to upload your files to a third-party server, ensuring your privacy.
- Completely free, without any hidden costs or limitations.
- Can be run locally on your computer without an internet connection.
- Easily customizable and extendable with the Python programming language.
- Faster processing, as the video is generated on your own machine.






