import facebook_scraper as fs
import csv
from time import sleep

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID"

""" pos id ya usados
pfbid0dRvWvuQ8auSMBx5M78wFWKPbTWnNwceBGyGmJ3HazN5iVBbGr9DwCtmvECQZHSvGl
pfbid0F96SixVCPLdeEAnwpSGQ6vi6CP5KkSTRDWa41A6ZN5uiLjEJXXCh5DrLDSMvB2uyl
631296762416090
pfbid0F96SixVCPLdeEAnwpSGQ6vi6CP5KkSTRDWa41A6ZN5uiLjEJXXCh5DrLDSMvB2uyl  
pfbid02HKtMFoCGx3ZawKq9qubQbMxf5An2WosJDbQfosbA1BPLQYn1i3Vo5ogo4AnvDgUNl
pfbid0MHEE3rgFoDsT32RnTgCVJDTumPxRqsquvyhweAkRWXpyTTsEqPnLsnFKZff2WqqQl
 pfbid0qKFuC9HaTKBFWZttRj42dy5Xbo6WdiqAMJFXF7Hd4K4gesHFr2X1HfyuXipugCQMl
 pfbid02c5qWkms7NGJnebdBvh3k2hDSPjd4Bue4ArEUve4iaW8QRDvRFgppaf98JXJCxPVpl
  pfbid0M8VTzQfBh3EypfJXTJKEnNHNYoDfHJneU11SbMgGWUvwHc2JuRibTMqoBU9WXsmnl
  pfbid0aHsTEHtvqBqiKTcvCcwMV3s6xrTUJKMJFkPzskDzADNXCBkU1vHWUgwfU2Y8cCN1l
"""

POST_ID = "pfbid0261rtkNW6EfkuDRMGwwQjfZUUXyFTfgz8oKQ5iWkWC2NJBf4p5erZDMN4YdGjKjLyl"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 500

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
