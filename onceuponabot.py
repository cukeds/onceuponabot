# Importing Libs
import praw
import pdb
import re
import random
import os


# Create Reddit Instance
reddit = praw.Reddit('bot1')

# Replied comments file creation
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# Reading replied comments file
else:
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split('\n')
        comments_replied_to = list(filter(None, comments_replied_to))

# Getting the subreddit
subreddit = reddit.subreddit("TownOfSalemGame")

# Checking the top 5 hottest boys from that spicy subreddit lawl
for submission in subreddit.hot(limit=5):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if comment.id not in comments_replied_to:
            if re.search('shut up exe', comment.body, re.IGNORECASE):
                print('Bot replying to :', comment.author)
                comment.reply(random.choice(['Cotton Mather','Deodat Lawson','Edward Bishop','Giles Corey','James Bayley',
                                            'James Russel','John Hathorne','John Proctor','John Willard','Jonathan Corwin',
                                            'Samuel Parris','Samuel Sewall','Thomas Danforth','William Hobbs',
                                            'William Phips']) + " was executed by the Jailor \n\n His role was Sheriff")
                comments_replied_to.append(comment.id)


# updating list

with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + '\n')
