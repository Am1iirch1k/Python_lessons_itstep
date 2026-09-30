import json
print("hello world")








# 05  Каталог игровых профилей
# Создайте players.json со списком из пяти словарей: id, nickname, level и active. Сохраните кириллицу читаемо и сделайте отступы.

players = [
    {"id":1, "nickname": "Ali", "level": 12, "active": True},
    {"id":2, "nickname": "Amirlan", "level": 125, "active": True},
    {"id":5, "nickname": "Dmitriy", "level": 221, "active": False},
    {"id":3, "nickname": "Danila", "level": 56, "active": False},
    {"id":4, "nickname": "Kanysh", "level": 10, "active": True},
    {"id":7, "nickname": "Damir", "level": 11, "active": False},
    {"id":9, "nickname": "Malika", "level": 83, "active": True},
    {"id":10, "nickname": "Ali", "level": 94, "active": False}
]

with open("players.json", "w", encoding="utf-8") as file:
    json.dump(players, file, ensure_ascii=False, indent=3)







# 06  Загрузка турнира
# Прочитайте players.json и выведите каждого игрока в формате: Mira — уровень 7 — активен. Для неактивного игрока выведите неактивен.

with open("players.json", "r", encoding="utf-8") as file:
    players = json.load(file)

for player in players:
    status = "active" if player["active"] else "not active"
    print(f"{player["nickname"]} - {player["level"]} level{status}")





# 07  Новый игрок
# Напишите функцию add_player(nickname, level), которая загружает players.json, создаёт следующий id, добавляет активного игрока и сохраняет файл.


def add_player(nickname, level):
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    new_id = max((player["id"] for player in players), default = 0) + 1

    players.append({"id": new_id, "nickname": nickname, "level": level, "active": True})
  
    with open("players.json", "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=3)

add_player("Ali213pro", 14)