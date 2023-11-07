import facebook_scraper as fs
import csv
from time import sleep

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID
POST_ID = "pfbid02X9A5QtZugbe5Sn5gUhoq17EMH4TC5vCZ7spo3kLifRg4EA1LKKF9xhELgsP5V1bKl"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 50

# get the post (this gives a generator)
gen = fs.get_posts(
    post_urls=[POST_ID],
    options={"comments": MAX_COMMENTS, "progress": True}
)

# take 1st element of the generator which is the post we requested
post = next(gen)

# extract the comments part
comments = post['comments_full']

file=open('claudia.csv',mode='a')

# process comments as you want...
coment_txt=[]
for comment in comments:
    
    print(comment['comment_text'])
    coment_txt.append(comment['comment_text'])

print("este es el segundo comentario : \n",len(coment_txt))

with open('claudia.txt', 'a', encoding='utf-8') as file:
    for item in coment_txt:
        file.write(item+ '\n')
