!pip install yt-dlp

import yt_dlp
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd

# Set Seaborn style for a polished look
sns.set_style("whitegrid")

#  Replace with the full YouTube channel URL
channel_url = 'https://www.youtube.com/c/Veritasium/videos'  # Change this to your fav channel

print("📡 Fetching channel data...\n")

# yt-dlp options to get video list only
ydl_opts = {
    'quiet': True,
    'extract_flat': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    channel_data = ydl.extract_info(channel_url, download=False)

videos = channel_data.get('entries', [])[:10]  # Limit to latest 10 videos

# Print basic info
print("🎬 Latest 10 Videos:\n")
for i, video in enumerate(videos):
    print(f"{i+1}. 🧠 {video['title']}")
    print(f"🔗 https://www.youtube.com/watch?v={video['id']}")
    print("-" * 60)

# Fetch view counts
print("\n🔍 Gathering views for each video...\n")
views = []
titles = []
video_urls = []

with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
    for video in videos:
        video_url = f"https://www.youtube.com/watch?v={video['id']}"
        info = ydl.extract_info(video_url, download=False)
        view_count = info.get('view_count', 0)
        views.append(view_count)
        titles.append(info.get('title', 'Untitled'))
        video_urls.append(video_url)
        print(f"📊 {info['title']} — {view_count:,} views")

# Sort by view count
sorted_data = sorted(zip(titles, views, video_urls), key=lambda x: x[1], reverse=True)
titles, views, video_urls = zip(*sorted_data)

# Create a DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Views': views,
    'URL': video_urls
})

#  Plot the chart
plt.figure(figsize=(12, 7))
colors = sns.color_palette("coolwarm", len(titles))
bars = plt.barh(titles, views, color=colors)
plt.xlabel("👀 View Count", fontsize=12)
plt.title("💥 Top 10 Most Viewed Videos (Latest Uploads)", fontsize=16, weight='bold')
plt.gca().invert_yaxis()
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1e6)}M' if x >= 1e6 else f'{int(x/1e3)}K'))
plt.tight_layout()
#  Add view count labels to bars
for bar, view in zip(bars, views):
    plt.text(bar.get_width() + 10000, bar.get_y() + bar.get_height()/2,
             f"{view:,}", va='center', fontsize=9, color='black')

plt.show()

# Optional: Save to CSV
df.to_csv("youtube_channel_analysis.csv", index=False)
print("\n✅ Data saved to youtube_channel_analysis.csv")
