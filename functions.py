import sqlite3


def select_query(query: str):
    con = sqlite3.connect("animal.db")
    cur = con.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    return results


animals = select_query("SELECT a.'index', a.color1, a.color2 FROM animals AS a")
colors = select_query("SELECT c.id, c.title_of_color FROM colors AS c")


def get_color_index(animal_color: str) -> int:
    for index, color in colors:
        if color == animal_color:
            return index


outcome = []  # (animal_id, color_id)

for index, color_1, color_2 in animals:
    if color_1:
        color_id = get_color_index(color_1)
        if color_id:
            outcome.append((index, color_id))
    if color_2:
        color_id = get_color_index(color_2)
        if color_id:
            outcome.append((index, color_id))

con = sqlite3.connect("animal.db")
cur = con.cursor()
for animal_id, color_id in outcome:
    cur.execute(f"INSERT INTO animal_colors(animal_id, color_id) VALUES({animal_id}, {color_id})")
    con.commit()
cur.close()
