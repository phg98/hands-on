
f = open("index.md", 'w', encoding='utf8')
message = '''# 핵토버페스트 서울 밋업 핸즈온 세션 저장소
핵토버페스트 서울 밋업의 핸즈온 세션 저장소 입니다.
번호를 누르면 해당 파일로 이동합니다.

'''
f.write(message)
for i in range(1, 27):
    data = "[{0}]({1}.md)\n".format(i, i)
    f.write(data)
f.close()


for i in range(1, 27):
    f = open(str(i)+".md", 'w')
    data = "[Hactoberfest Seoul Meetup!](https://event-us.kr/hacktoberfestseoul/event/23432)"
    f.write(data)
    f.close()