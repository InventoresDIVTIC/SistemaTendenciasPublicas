import facebook_scraper as fs
import csv
from time import sleep

# Get POST_ID from the URL of the post, e.g., https://www.facebook.com/USER/posts/POST_ID
POST_ID = "https://www.facebook.com/Latinus/videos/631296762416090/"

# Number of comments to download; set this to True to download all comments
MAX_COMMENTS = 500

# Get the post (this gives a generator)
gen = fs.get_posts(post_urls=[POST_ID], options={"comments": MAX_COMMENTS, "progress": True})

# Take the first element of the generator, which is the post we requested
post = next(gen)

# Extract the comments part


file = open('claudia.csv', mode='a')

# Process comments as you want...

# Check if the post contains a video
if 'video' in post:
    video_url = post['video']
    print(f"This post contains a video. Video URL: {video_url}")

    # Now, extract comments from the video post
    video_comments = fs.get_video_comments(video_url, options={"comments": MAX_COMMENTS, "progress": True})

    # Process video comments as you want...
    video_comment_text = []
    for video_comment in video_comments:
        print(video_comment['comment_text'])
        video_comment_text.append(video_comment['comment_text'])

    print("Estos son los comentarios del video:\n", len(video_comment_text))

    with open('claudia_video_comments.txt', 'a', encoding='utf-8') as file:
        for item in video_comment_text:
            file.write(item + '\n')
else:
    print("This post does not contain a video.")
