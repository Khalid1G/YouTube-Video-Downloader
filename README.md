# YouTube Video Downloader

This script allows you to list and download video streams from YouTube using the `yt-dlp` library. You can choose the desired format and download location for the video.

## Requirements

- Python 3.6+
- `yt-dlp` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Khalid1G/youtube_video_downloader.git
   cd youtube_video_downloader
   ```

2. **Create a virtual environment (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the `yt-dlp` library:**

   ```bash
   pip install yt-dlp
   ```

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Enter the YouTube video URL:**

   The script will prompt you to enter the URL of the YouTube video you want to download.

3. **List available video streams:**

   The script will list all available video streams for the provided URL.

4. **Enter the format code:**

   Choose the format code of the desired stream from the listed streams.

5. **Enter the download path:**

   Specify the path where you want to save the video. If you don't provide a path, the video will be saved in the `./downloads` directory by default.

## Example

1. **Run the script:**

   ```bash
   python youtube_downloader.py
   ```

2. **Enter the YouTube video URL:**

   ```
   Enter the YouTube video URL: https://www.youtube.com/watch?v=3UbjgjfYC-I
   ```

3. **List available video streams:**

   ```table
   ID  EXT   RESOLUTION FPS CH │   FILESIZE   TBR PROTO │ VCODEC          VBR ACODEC      ABR ASR MORE INFO
   ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   sb3 mhtml 48x27        0    │                  mhtml │ images                                  storyboard
   sb2 mhtml 80x45        1    │                  mhtml │ images                                  storyboard
   sb1 mhtml 160x90       1    │                  mhtml │ images                                  storyboard
   sb0 mhtml 320x180      1    │                  mhtml │ images                                  storyboard
   233 mp4   audio only        │                  m3u8  │ audio only          unknown             Default
   234 mp4   audio only        │                  m3u8  │ audio only          unknown             Default
   139 m4a   audio only      2 │    1.31MiB   49k https │ audio only          mp4a.40.5   49k 22k low, m4a_dash
   249 webm  audio only      2 │    1.38MiB   51k https │ audio only          opus        51k 48k low, webm_dash
   250 webm  audio only      2 │    1.82MiB   68k https │ audio only          opus        68k 48k low, webm_dash
   140 m4a   audio only      2 │    3.49MiB  129k https │ audio only          mp4a.40.2  129k 44k medium, m4a_dash
   251 webm  audio only      2 │    3.60MiB  134k https │ audio only          opus       134k 48k medium, webm_dash
   602 mp4   256x144     13    │ ~  2.24MiB   83k m3u8  │ vp09.00.10.08   83k video only
   394 mp4   256x144     25    │    1.53MiB   57k https │ av01.0.00M.08   57k video only          144p, mp4_dash
   269 mp4   256x144     25    │ ~  4.33MiB  161k m3u8  │ avc1.4D400C    161k video only
   160 mp4   256x144     25    │    1.70MiB   63k https │ avc1.4D400C     63k video only          144p, mp4_dash
   603 mp4   256x144     25    │ ~  4.18MiB  155k m3u8  │ vp09.00.11.08  155k video only
   278 webm  256x144     25    │    2.26MiB   84k https │ vp9             84k video only          144p, webm_dash
   395 mp4   426x240     25    │    2.89MiB  107k https │ av01.0.00M.08  107k video only          240p, mp4_dash
   229 mp4   426x240     25    │ ~  7.08MiB  263k m3u8  │ avc1.4D4015    263k video only
   133 mp4   426x240     25    │    2.83MiB  105k https │ avc1.4D4015    105k video only          240p, mp4_dash
   604 mp4   426x240     25    │ ~  7.82MiB  290k m3u8  │ vp09.00.20.08  290k video only
   242 webm  426x240     25    │    3.97MiB  148k https │ vp9            148k video only          240p, webm_dash
   396 mp4   640x360     25    │    5.47MiB  203k https │ av01.0.01M.08  203k video only          360p, mp4_dash
   230 mp4   640x360     25    │ ~ 13.83MiB  513k m3u8  │ avc1.4D401E    513k video only
   134 mp4   640x360     25    │    5.14MiB  191k https │ avc1.4D401E    191k video only          360p, mp4_dash
   18  mp4   640x360     25  2 │   15.13MiB  562k https │ avc1.42001E         mp4a.40.2       44k 360p
   605 mp4   640x360     25    │ ~ 15.24MiB  566k m3u8  │ vp09.00.21.08  566k video only
   243 webm  640x360     25    │    6.92MiB  257k https │ vp9            257k video only          360p, webm_dash
   397 mp4   854x480     25    │    9.10MiB  338k https │ av01.0.04M.08  338k video only          480p, mp4_dash
   231 mp4   854x480     25    │ ~ 18.57MiB  689k m3u8  │ avc1.4D401E    689k video only
   135 mp4   854x480     25    │    7.70MiB  286k https │ avc1.4D401E    286k video only          480p, mp4_dash
   606 mp4   854x480     25    │ ~ 23.55MiB  874k m3u8  │ vp09.00.30.08  874k video only
   244 webm  854x480     25    │   10.07MiB  375k https │ vp9            375k video only          480p, webm_dash
   398 mp4   1280x720    25    │   16.03MiB  596k https │ av01.0.05M.08  596k video only          720p, mp4_dash
   232 mp4   1280x720    25    │ ~ 29.39MiB 1091k m3u8  │ avc1.4D401F   1091k video only
   136 mp4   1280x720    25    │   13.82MiB  514k https │ avc1.4D401F    514k video only          720p, mp4_dash
   609 mp4   1280x720    25    │ ~ 38.77MiB 1439k m3u8  │ vp09.00.31.08 1439k video only
   247 webm  1280x720    25    │   15.16MiB  564k https │ vp9            564k video only          720p, webm_dash
   399 mp4   1920x1080   25    │   27.18MiB 1010k https │ av01.0.08M.08 1010k video only          1080p, mp4_dash
   270 mp4   1920x1080   25    │ ~106.27MiB 3945k m3u8  │ avc1.640028   3945k video only
   137 mp4   1920x1080   25    │   48.26MiB 1794k https │ avc1.640028   1794k video only          1080p, mp4_dash
   614 mp4   1920x1080   25    │ ~ 70.56MiB 2619k m3u8  │ vp09.00.40.08 2619k video only
   248 webm  1920x1080   25    │   29.12MiB 1083k https │ vp9           1083k video only          1080p, webm_dash
   616 mp4   1920x1080   25    │ ~137.89MiB 5118k m3u8  │ vp09.00.40.08 5118k video only          Premium
   ```

4. **Enter the format code:**

   ```
   Enter the format code of the desired stream: 615
   ```

5. **Enter the download path:**

   ```
   Enter the download path (default is current directory): ./videos
   ```

6. **Download completed:**

   ```
   Download completed!
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
