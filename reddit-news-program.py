import praw
r = praw.Reddit(user_agent='my_news_application')
submissions = r.get_subreddit('news').get_hot(limit=10)

#output = [str(x) for x in submissions]

#output.strip(":")
#print output

for x in submissions:
	print x
	print "\n"

#need to work on this a bit more 
