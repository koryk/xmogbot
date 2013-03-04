import praw
import sys
import time
import creds


user_agent = "asoiaf post bot"
thing_limit = 15 


r = praw.Reddit(user_agent=user_agent)
r.login(creds.uid,creds.pw)
xmog = r.get_subreddit('testasoiaf')
print '''logged in'''

got = ['agot', 'got']
cok = ['acok','cok']
asos = ['asos','sos']
affc = ['affc','ffc'] 
adwd = ['adwd','dwd']
twow = ['twow','wow']
all = ['all']
de = ['d&e','d&amp;e','dunk&amp;egg']
types = [got,cok,asos,affc,adwd,twow,de,all]
crow = ['crow business']
none = ['no spoilers', 'no spoiler']
others = [crow, none]

updated = """Your friendly neighbourhood flairbot added flair to your post
            automatically. If your flair is in error, please do not
            hesitate to tell a moderator about it. Your post has been marked as spoiler level: """


# already taken care of = atco
# f = flair
# i = item list
atcof = []
atcoi = []


def checkarmor(type, submission, beforetext):
    if any (beforetext + word in submission.title.lower() for word in type):
        print 'setting flair for ' + submission.id + ' to ' + type[0].upper()
        try:
            submission.set_flair(type[0].upper(),type[0].replace('&',''))
            #submission.add_comment(updated + type[0].upper() + '.')
            atcof.append(submission.id)
        except Exception, e:
            print 'did not add flair ', sys.exc_info()[0]
	    print e;


running = True
while (running):
    for submission in xmog.get_hot(limit=thing_limit):
	print 'checking submission ' + submission.title;
        if (submission.link_flair_text == None and submission.id not in atcof):
            for type in types:
                checkarmor(type, submission, 'spoilers ')
	    for type in others:
		checkarmor(type, submission, '')
    time.sleep(600)
