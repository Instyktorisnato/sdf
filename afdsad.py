# smart_notes

# file = open("test.txt", "w", encoding="utf-8")
# file.write("Hello world!")

# file = open("test.txt", "r", encoding="utf-8")
# data = file.read()
# print(data)

# file = open("test.txt", "a", encoding="utf-8")
# for i in range(100):
#     file.write("Hello\n")
#
# file.close()

with open("test.txt", "r", encoding="utf-8") as file:
    data = file.read()
