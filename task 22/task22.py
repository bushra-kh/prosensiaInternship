import requests
import pandas as pd
import matplotlib.pyplot as plt
import logging
import sys

logging.basicConfig(filename="yt_log.txt", level=logging.ERROR, format="%(asctime)s %(levelname)s:%(message)s")

API_KEY = "AIzaS.....zwAugz9PSc"  # API key

def get_video_id(url):
    try:
        if "v=" in url:
            return url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
        else:
            raise ValueError("Invalid YouTube URL")
    except Exception as e:
        logging.error(f"URL parsing error: {e}")
        return None

def fetch_stats(video_id):
    try:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={API_KEY}"
        resp = requests.get(url)
        data = resp.json()
        item = data["items"][0]
        title = item["snippet"]["title"]
        stats = item["statistics"]
        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))
        comments = int(stats.get("commentCount", 0))
        return {"Title": title, "Views": views, "Likes": likes, "Comments": comments}
    except Exception as e:
        logging.error(f"API error for {video_id}: {e}")
        return None

def main():
    print("Enter YouTube video URLs (one per line). Type 'done' to finish:")
    urls = []
    while True:
        url = input()
        if url.lower() == "done":
            break
        urls.append(url)
    results = []
    for url in urls:
        vid = get_video_id(url)
        if not vid:
            print(f"Invalid URL: {url}")
            continue
        stats = fetch_stats(vid)
        if stats:
            results.append(stats)
            print(f"Fetched: {stats['Title']}")
        else:
            print(f"Failed to fetch stats for: {url}")
    if results:
        df = pd.DataFrame(results)
        df.to_csv("yt_stats.csv", index=False)
        print("Saved stats to yt_stats.csv")
        # Plot
        plt.figure(figsize=(8,4))
        df.plot(x="Title", y=["Views", "Likes", "Comments"], kind="bar")
        plt.title("YouTube Video Stats")
        plt.tight_layout()
        plt.savefig("yt_stats_chart.png")
        print("Saved chart to yt_stats_chart.png")
    else:
        print("No results to save.")

if __name__ == "__main__":
    main()