# ImageSequenceTranscoder

[![GitHub license](https://img.shields.io/github/license/L0Lock/ImageSequenceTranscoder?style=for-the-badge&logo=#007808)](https://github.com/L0Lock/ImageSequenceTranscoder/blob/master/LICENSE)  [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H818FHX)

Image Sequence Transcoder (IST) is an artist-friendly tool to quickly transcode your image sequences into video files. It uses FFmpeg for transcoding and is written using Python and PySide6.

No need to know what settings to use, they are reduced down to the main ones you most often need and are easil worded for ease of use.

## Installation

- Download the [latest release](https://github.com/L0Lock/ImageSequenceTranscoder/releases/latest) and unpack it wherever you want. You should have an icon file and a python file.
- If you don't have FFmpeg already, download the [lastest "static" ffmpeg pack](https://ffmpeg.zeranoe.com/builds/). You can either put the ffmpeg executable alongside the main .py file or anywhere you want.

## Usage

![application screenshot](https://github.com/L0Lock/ImageSequenceTranscoder/blob/main/Prez/AppScreenshot.jpg)

1. indicate the location of your ffmpeg binary file. IST will automatically remember this next time your run it, so you will need to do this only once.

2. Locate your image sequence path. Select the first frame from which you want the image sequence to be encoded.

3. Optional: Locate and audio file. If you don't put anything, IST will try to find an audio file named `audio.mp3` alongside your frames. If no audio is provided, it will encode your video without audio.

4. Optional: Chose an output path and file name with extension. If nothing provided, it will output an MP4 file alongside your frames with the original frame name and a timestamp at the end.
   If you want a different container like MKV or MOV, simply write `.mkv` or `.mov` as the file extension.

5. Set your video options. default settings is for a standard H264 video like everywhere in the Internet with balanced quality/speed settings for most usages, so the most important thing is to **check the framerate**.

6. Set your audio codec. Either copy the stream as-is without conversion, or re-encode it. Unless you have a .wav or a .flac, I'd advise to copy.
