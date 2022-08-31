# Задание 1:
# Создать файл с текстом, а затем написать программу, которая будет считывать
# текст из файла выбирая только нужные слова и поместить данные слова в отдельный документ

def createFile(nameFile, modeFile, textFile):
    if modeFile == "w":
        with open(nameFile, modeFile) as file:  # with- автоматически открывает и закрывает файл
            file.write(str(textFile))
        print("File write" + nameFile)
    else:
        with open(nameFile, modeFile) as file:
            print(file.read())
        print("File write" + nameFile)

text = \
    (
    "Create a file with text, and then write a program that will read the text \n"
    "from the file, selecting only the necessary words and place these words in a separate document"
    )
# print(text)
# Создаем файл ("Имя", "W" - режим записи, переменную)
createFile("filehw7.txt", "w", text)

text = text.split() # split() - выделить слова отдельно
for x in text:
    if x == "text":
        createFile("goodFile.txt", "w", text)


# Задание 2:
# Закрепить работу с json файлами, создать простенький json файл и затем его прочитать.

import json

jsonText =  {
    "family": {
        "maksim": {
            "first_name": "Maksim",
            "Last_name": "Shalaputov",
            "location": "Chelyabinsk",
            "age": "34"
        },
        "Anastasia": {
            "first_name": "Anastasia",
            "Last_name": "Shalaputov",
            "location": "Chelyabinsk",
            "age": "25"
        },
        "Victor": {
            "first_name": "Victor",
            "Last_name": "Shalaputov",
            "location": "Chelyabinsk",
            "age": "2"
        }
    }
}


def createFile(nameFile, modeFile, *textFile):

    if modeFile == "w":
        with open(nameFile, modeFile) as file:
            file.write(str(textFile))
        print("File write" + str(nameFile))
    else:
        with open(nameFile, modeFile) as file:
            print(file.read())
        print("File write" + str(nameFile))

createFile("FILE_JSON.json", "w", jsonText)  # indent=4 в какой момент его использовать?

createFile("FILE_JSON.json", "r")


for x in jsonText("family"):
    print("first_name: ", x["Maksim"])

# pass # TODO pass - разобраться в логике прочтения Json через функцию




