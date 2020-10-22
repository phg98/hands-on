
f = open("index.md", 'w')
for i in range(1, 21):
    data = "[{0}]({1}.md)".format(i, i)
    f.write(data)
f.close()
exit()


for i in range(1, 21):
    f = open(str(i)+".md", 'w')
    data = "[Hactoberfest Seoul Meetup!](https://event-us.kr/hacktoberfestseoul/event/23432)"
    f.write(data)
    f.close()