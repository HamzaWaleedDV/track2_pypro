import ezgmail, os
from pathlib import Path

os.chdir(Path('E:\Back-End(hsoub)', 'Projects(Track 2)', 'Gmail'))
ezgmail.init()

print(ezgmail.EMAIL_ADDRESS)

# ezgmail.send('hamzawaleed061@gmail.com', 'Test', 'hello hamza how are you??', ['test.jpg', 'test1.jpg'])

unreadMessage = ezgmail.unread()
# print(ezgmail.summary(unreadMessage))
# print(len(unreadMessage))
# print(unreadMessage[0].messages[0])
# print(unreadMessage[0].messages[0].subject)
# print(unreadMessage[0].messages[0].body)
# print(unreadMessage[0].messages[0].timestamp)
# print(unreadMessage[0].messages[0].sender)
# print(unreadMessage[0].messages[0].recipient)

recentThreads = ezgmail.recent()
# print(ezgmail.summary(recentThreads))
print(len(recentThreads))


recentThreads = ezgmail.recent(maxResults=654)
print(len(recentThreads))

result = ezgmail.search('hsoub academy')
print(len(result))