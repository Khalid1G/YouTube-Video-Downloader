import yt_dlp
from urllib.parse import urlparse, parse_qs


def is_playlist_url(url):
    """
    Check if a URL is for a YouTube playlist.
    """
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)
    return "list" in query.keys()


def list_video_streams(url):
    """
    List available video streams for a given YouTube video URL.
    """
    try:
        ydl_opts = {"listformats": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"An error occurred: {e}")


def download_single_video(url, format_code, path="."):
    """
    Download a single video from a YouTube URL with a specified format code.
    """
    try:
        ydl_opts = {"format": format_code, "outtmpl": f"{path}/%(title)s.%(ext)s"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_playlist(url, path="."):
    """
    Download an entire YouTube playlist.
    """
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{path}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
            "noplaylist": False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")

    if is_playlist_url(video_url):
        download_path = (
            input("Enter the download path (default is './downloads'): ")
            or "./downloads"
        )
        download_playlist(video_url, download_path)
    else:
        print("Listing available video streams:")
        list_video_streams(video_url)

        format_code = input("Enter the format code of the desired stream: ")
        download_path = (
            input("Enter the download path (default is './downloads'): ")
            or "./downloads"
        )

        download_single_video(video_url, format_code, download_path)
