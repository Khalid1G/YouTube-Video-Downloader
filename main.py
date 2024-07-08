import yt_dlp


# Function to list available video streams
def list_video_streams(url):
    try:
        # Set options for yt-dlp to list available formats
        ydl_opts = {"listformats": True}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print(f"An error occurred: {e}")


# Function to download the selected stream
def download_video(url, format_code, path="."):
    try:
        # Set options for yt-dlp
        ydl_opts = {"format": format_code, "outtmpl": f"{path}/%(title)s.%(ext)s"}

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")


video_url = input("Enter the YouTube video URL: ")

print("Listing available video streams:")
list_video_streams(video_url)

format_code = input("Enter the format code of the desired stream: ")
download_path = (
    input("Enter the download path (default is current directory): ") or "./downloads"
)

download_video(video_url, format_code, download_path)
