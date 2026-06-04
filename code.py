from datetime import datetime
import pandas as pd

# Titel Tabelle befüllen

title_query = """
INSERT INTO Title
(show_id, title, date_added,
 country_name,
 release_year, description, rating, duration, genre)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Datum von z.b Septmeber 2016 zu Date values die gespeichert werden können
def parse_date(x):
    if pd.isna(x):
        return None

    try:
        return datetime.strptime(x, "%B %d, %Y").date()
    except Exception:
        return None


for _, row in df.iterrows():
    cursor.execute(
        title_query,
        (
            row["show_id"],
            row["title"],
            parse_date(row["date_added"]),
            row["country"] if not pd.isna(row["country"]) else None,
            row["release_year"] if not pd.isna(row["release_year"]) else None,
            row["description"],
            row["rating"] if not pd.isna(row["rating"]) else None,
            row["duration"] if not pd.isna(row["duration"]) else None,
            row["listed_in"] if not pd.isna(row["listed_in"]) else None,
        ),
    )
# Director und directs Tabelle befüllen
director_id_map = {}
next_director_id = 1

director_insert = """
INSERT INTO Director (director_id, director_name)
VALUES (%s, %s)
"""

directs_insert = """
INSERT INTO Directs (director_id, show_id)
VALUES (%s, %s)
"""

for _, row in df.iterrows():

    if pd.isna(row["director"]):
        continue

    directors = [d.strip() for d in row["director"].split(",")]

    for d in directors:

        if d not in director_id_map:
            director_id_map[d] = next_director_id

            cursor.execute(
                director_insert,
                (next_director_id, d)
            )

            next_director_id += 1

        # Many-to-many relationship
        cursor.execute(
            directs_insert,
            (director_id_map[d], row["show_id"])
        )

#Actor und casts Tabelle befüllen

actor_id_map = {}
next_actor_id = 1

actor_insert = """
INSERT INTO Actor (actor_id, actor_name)
VALUES (%s, %s)
"""

casts_insert = """
INSERT INTO Casts (actor_id, show_id)
VALUES (%s, %s)
"""

for _, row in df.iterrows():

    if pd.isna(row["cast"]):
        continue

    actors = [a.strip() for a in row["cast"].split(",")]

    for a in actors:

        if a not in actor_id_map:
            actor_id_map[a] = next_actor_id

            cursor.execute(
                actor_insert,
                (next_actor_id, a)
            )

            next_actor_id += 1

        cursor.execute(
            casts_insert,
            (actor_id_map[a], row["show_id"])
        )

conn.commit()
cursor.close()
conn.close()