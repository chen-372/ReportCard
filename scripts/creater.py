from csv import DictReader
from sqlite3 import connect

print("connecting to database...")
connection = connect("databases/report_cards.sqlite")

print("creating the table...")

connection.execute(
    """
    CREATE TABLE results (
        id          INTEGER PRIMARY KEY,
        student_id  CHARACTER(3),
        subject_id  CHARACTER(4),
        teacher_id  CHARACTER(3),
        criterion   CHARACTER(1),
        score       INTEGER
    );
"""
)

print("inserting data...")
with open("data/results.csv") as f:
    reader = DictReader(f)
    for row in reader:
        connection.execute(
            "INSERT INTO results VALUES (?, ?, ?, ?, ?, ?);",
            (
                row["id"],
                row["student_id"],
                row["subject_id"],
                row["teacher_id"],
                row["criterion"],
                row["score"],
            ),
        )


connection.commit()
connection.close()
