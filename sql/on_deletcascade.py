import sqlite3

with open('schema.sql') as fobj:
    schema = fobj.read()

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
# Foreign key support is not enabled in SQLite by default.
cur.execute('PRAGMA foreign_keys = ON')
cur.executescript(schema)

buildings = cur.execute('SELECT * FROM buildings').fetchall()
print('== Buildings')
print(buildings)

rooms = cur.execute('SELECT * FROM rooms').fetchall()
print('== Rooms')
print(rooms)

delete_building = cur.execute('DELETE FROM buildings WHERE building_no = 2')
print('== DELETED buildings.building_no = 2')

buildings = cur.execute('SELECT * FROM buildings').fetchall()
print('== Buildings')
print(buildings)

rooms = cur.execute('SELECT * FROM rooms').fetchall()
print('== Rooms')
print(rooms)

# Cleanup even if this is a short-lived script.
conn.close()
