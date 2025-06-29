YOUTUBE CHANNEL ANALYSIS

Hey there! 
This little script — DA.py — is like a data detective for YouTube.
You give it a YouTube channel, and it gives you back the latest 10 videos, sorted by view count, all wrapped in a pretty bar chart. 

What does DA.py do?
  - Connects to a YouTube channel’s video tab

  - Extracts the latest 10 videos using yt-dlp

  - Fetches each video’s title, view count, and link

  - Visualizes it all in a colorful horizontal bar chart

  - Saves a .csv file so you can explore the data later

It’s simple, visual, and surprisingly satisfying to see which videos are performing best.

How to use it
1. Install the libraries
  pip install yt-dlp matplotlib seaborn pandas
2. Open DA.py
  Change the channel_url to your favorite channel’s Videos tab:
  channel_url = 'https://www.youtube.com/c/Veritasium/videos'
3. Run the script
  python DA.py

What you'll see
  - A list of 10 video titles + links in your terminal
  - A stylish chart of view counts
  - A CSV file: youtube_channel_analysis.csv with full data

Output Example (Console)
Latest 10 Videos:

1. 🧠 Why You Don’t Hear About Dark Matter Anymore
🔗 https://youtube.com/watch?v=abc123
...
Then comes your chart!

About Me
I'm Aishwarya Kotagiri
