# Задание:
# 1. Вывести данные из файла json, а именно id, name, age, gender, balance, email, phone, isActive
# 2. Отсортировать полученные данные по полю isActive, записать полученный результат в файл result.txt
# 3. Осортировать по возрастанию balance только активных пользователей,записать полученный результат в файл result.txt
# 4. Опубликовать работу на гитхаб. Репозиторий: https://github.com/LessonsTop/practic-1
# в ветки practic_FI (Где FI - фамилия и имя).

import json

jsonDocument = "generated.json"

# Необходимо открыть файл
f = open(jsonDocument, 'r')  # 'r' -  чтение
jsonData = json.load(f)      # Загружаем наш файл
f.close                      # Закрываем его и можно с ним работать

print(jsonData)
listText = []
# Делаем 'Парсинг данных' - получаем данные и распределяем их по формату
# Задание 1: смотреть условие.
for x in jsonData:

    print("id: ", x["_id"])
    print("name: ", x["name"])
    print("age: ", x["age"])
    print("gender: ", x["gender"])
    print("balance: ", x["balance"])
    print("email: ", x["email"])
    print("phone: ", x["phone"])
    print("isActive: ", x["isActive"])
    print("=="*20)      # отделяем пользователей

    info = {

        "_id": x['_id'],
        "name": x["name"],
        "age": x["age"],
        "gender": ["gender"],
        "balance": x["balance"],
        "email": x["email"],
        "phone": x["phone"],
        "isActive": x["isActive"]

    }

    listText.append(info)

f = open('result.txt', 'w')
listText.sort(key=lambda row: row["isActive"])
text = str(listText)
f.write(text)
f.close()
print(listText)

f = open('result1.txt', 'w')

ListPersonTrue = list(filter(lambda row: row["isActive"] == True, listText))

ListPersonTrue.sort(key=lambda row: row['balance'], reverse=True)

text = str(listText)
f.write(text)
f.close()
print(listText)
for x in ListPersonTrue:
    print(x)

    














