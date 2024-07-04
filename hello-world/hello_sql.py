import os
import sqlite3
from functools import reduce


PATH_TO_DB = "../"
db_files = []

con = sqlite3.connect("chinook.db")
cur = con.cursor()

res = cur.execute(
    """SELECT trackId, name
    FROM tracks
    LIMIT 5"""
)

for row in res:
    print(row)

sql_command = ""
with open("hello-world/hello.sql", "r") as sql_file:
    lines = sql_file.readlines()
    print(lines)

    sql_command = reduce(lambda first_line, next_line: first_line + next_line, lines)
    print(sql_command)


for result in cur.execute(sql_command):
    print(result)
