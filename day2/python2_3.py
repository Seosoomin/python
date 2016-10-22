#for

a= [1,2,3]

for i in a:
    print(i)

#i는 list의 구성요소
    # 아래의 경우는 dictionary를 의미함
list = [{"name":"가"}, {"name":"나"}, {"name":"다"}]
for i in list:
    print(i)


list2 = [{"name":"가","score":40}, {"name":"나","score":60}]
for i in list2:
    print(i["name"]+"의 점수는 " + str(i["score"]))

index = 1
list3 = [{"name":"홍길동","score":40}, {"name":"황진희","score":60}]
for i in list3:
    print(str(index) + "번째: " + i["name"] + "의 점수는 " + str(i["score"]))
    index = index + 1


#점수 50이상 합격
index = 1
for i in list3:
    if i["score"] >= 50:
    print("str(index)" + "번째: " + i["name"] + "합격")
else:
    print("str(index)" + "번째: " + i["name"] + "불합격")
index = index + 1
