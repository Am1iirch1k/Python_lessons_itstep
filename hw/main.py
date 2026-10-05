def find_player(player_id):

    load_data = [
        {"id": 1, "nickname": "Mira", "level": 7, "active": True},
        {"id": 2, "nickname": "Orion", "level": 4, "active": False}
    ]

    for player in load_data:
        if player["id"] == player_id:
            return player
    return None


print(find_player(2))
print(find_player(99))



# 09  Повышение уровня
# Напишите функцию level_up(player_id), которая увеличивает level на 1, сохраняет изменения и возвращает True. Если игрок не найден, верните False.


def level_up(player_id):

    levels = [
        {"id": 1, "nickname": "Ali", "level": 8, "active": True},
        {"id": 2, "nickname": "Kanysh", "level": 2, "active": False}
    ]

    for level in levels:
        if level["id"] == player_id:
            level["level"] += 1
            return level
    return False

print(level_up(43))
print(level_up(8))




# 10  Архив профиля
# Напишите функцию deactivate_player(player_id), которая меняет active на False и сохраняет данные. Удалять запись не нужно.



def deactive_player(player_id):

    actives = [
        {"id": 1, "nickname": "Ali", "level": 8, "active": True},
        {"id": 2, "nickname": "Kanysh", "level": 2, "active": False}
    ]


    for active in actives:
        if active["active"] == player_id:
            active["active"] == False
            return active
    return False

print(deactive_player(2))
print(deactive_player(12))
print(deactive_player(8))


