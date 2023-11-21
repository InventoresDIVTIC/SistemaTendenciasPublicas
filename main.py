import facebook_scraper as fs
import csv
from time import sleep

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID"

""" pos id ya usados
pfbid02ZBYoe3rWzDrTeaM2GshtBCZZDcG8Vzv6TFyEGZdzXxBSaUjuSBGVCgnmnqeuauwzl
pfbid028NVERViFrtRXduuN4QGk4WrdD7MffrSaYH8sWwrBrALxoFDSoSNjKaeSFS3gGB8Cl
pfbid02Po8tMkW14hKEoq1Yr4ze6BmQfHvcuFK1drrgbpF6P45gEPaXXWunpKt6gKzCGeBxl
pfbid0cSp1WVi7HPRFWGV2u5Jtqswku2rpFX5Bo5wjzmcKDReAaL1DdctYHTxuN5RwfM25l
pfbid02ATAUzD47sRNe7UYBSWj8nDsN29vAPwP5xmGTWawR7zyqhkdpnRBASh2M3TBMv7fJl
pfbid02K1XMqLKoJv9HuFaNWQdFENvsH3tYab52LxA5X6o5oHHXGKdbayUjqFgtURe6Xj1Hl
pfbid0KbVMMawsTnjruvbnJqAnwmxKgZf9eDwM4tM8RUmysoHyArrHoQUboXVxB6p5UHhAl
pfbid0BUFMzJuTPR63EK4vAGEPJNPogpJTgCzjQEo4V5s3RnSSsj13nZ1qTfpV7qrmQE34l
pfbid02vfdsSVP1gYmdhf4nVR8Vd8jRH7MTUvyimvyDUXRKKjxszwtqrvGtqNbFQPbwfZAWl
pfbid02QikyKG5LtjZBYaz1PK3EYLrEE65AbkmSCCNiZDPisWv6oWbZFe24ZY7Aips7ymdGl
pfbid0DRwFVHaqpdx1pEFwsevPx9cB2jEGPNjVbVG9JaQb2RpEHay7Fq3F3cVpu8FirgxMl
pfbid02Jm7GjpLec1JPto6Vr2ankZNRQSMDz6A4AEiNrwavaHmAHSJZ3zPxMpaNMYCwU9Yvl
pfbid0B8NYKRYURXnVQL5zVzCQRn7jSrEiEP5Wvj2At5hQmXJ5gTMZaSkTZBjEdXrcYZYGl
pfbid0FZztMWxpT4Y1Jz7eQnxEoaZ2GnEVvkk65KL3KKHLApVgQfLFUy42Fg8QcCPTz5MPl
"""

POST_ID = "pfbid0FZztMWxpT4Y1Jz7eQnxEoaZ2GnEVvkk65KL3KKHLApVgQfLFUy42Fg8QcCPTz5MPl"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 100

# get the post (this gives a generator)
gen = fs.get_posts(
    post_urls=[POST_ID],
    options={"comments": MAX_COMMENTS, "progress": True}
)

# take 1st element of the generator which is the post we requested
post = next(gen)

# extract the comments part
comments = post['comments_full']

#file=open('claudia.csv',mode='a')

# process comments as you want...
coment_txt=[]
for comment in comments:
    
    print(comment['comment_text'])
    coment_txt.append(comment['comment_text'])

#print("este es el segundo comentario : \n",len(coment_txt))

with open('cucei.txt', 'a', encoding='utf-8') as file:
    for item in coment_txt:
        file.write(item+ '\n')
