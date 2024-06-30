# # # # # # # # # b = True
# # # # # # # # # print(b)
# # # # # # # # # b = False
# # # # # # # # # print(b)
# # # # # # # # # a=10
# # # # # # # # # print(a, id(a))
# # # # # # # # # a = 20
# # # # # # # # # print(a, id(a))

# # # # # # # # # x=[1,2,3,4]
# # # # # # # # # print(x, id(x))
# # # # # # # # # x.append(99)
# # # # # # # # # print(x, id(x))
# # # # # # # # a=1
# # # # # # # # print(a, type(a))
# # # # # # # # a = "1"
# # # # # # # # print(a, type(a))
# # # # # # # # a = [1,2,3]
# # # # # # # # print(a, type(a))
# # # # # # # # a=1.1234567
# # # # # # # # print(a)
# # # # # # # # print(round(a, 5))
# # # # # # # # print(round(a, 2))

# # # # # # # a = (1 + 2 + 3
# # # # # # # + 3 + 8
# # # # # # # - 7)
# # # # # # # print(a)

# # # # # # # a = ("test1",
# # # # # # #      "test2")
# # # # # # # print(a); print("My name is")

# # # # # # name = "Ivanna"

# # # # # # x, y, z = 1, 2, 3
# # # # # # print("name="+ name, x, y, z)

# # # # # # info = ("Ivanna", 42, "Iv-FR")
# # # # # # name, age, city = info
# # # # # # print(name, age, city)

# # # # # # # a=[1,2,3]
# # # # # # # b=a
# # # # # # # a.append(55)
# # # # # # # b[2]=88
# # # # # # # print(a,b)
# # # # # # # print(id(a))
# # # # # # # print(id(b))

# # # # # x=True
# # # # # c=0b10001
# # # # # print(x, c)

# # # # # l = [1, "12", 1.5, None]
# # # # # for i in l:
# # # # #     print(i, type(i))

# # # # s = {1, 22, 34, 34, 22, 5, 67, 8, 8, 98}
# # # # print(s)
# # # # print(22 in s)

# # # d={12: "value_12", "key":None}
# # # print(d)
# # # print(d[12])
# # # print(d["key"])

# # a = 1
# # print(a, type(a) is int, type(a))

# line = "123456"
# print(line, type(line))
# x=int(line)
# print(x, type(x))

# x=int("abc",16)
# print(x)

# for i in range (260):
#     print(i, "", chr(i))

# for i in "dsgdsgsgsd.,+_)":
#     print(i, "", ord(i))

# print("Hello world!!!")
# print(r"Hello \n world!!!")

template = "{} is {} years old. Your salary is {}"
name = "Jhon"
age = 30
salary = 4500
print(template.format(name, age, salary))
