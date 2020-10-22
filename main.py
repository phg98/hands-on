for i in range(1, 21):
    f = open(str(i)+".md", 'w')
    data = "[Hactoberfest Seoul Meetup!](https://event-us.kr/hacktoberfestseoul/event/23432)"
    f.write(data)
    f.close()