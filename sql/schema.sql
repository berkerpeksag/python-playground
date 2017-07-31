CREATE TABLE IF NOT EXISTS buildings (
    building_no INTEGER PRIMARY KEY AUTOINCREMENT,
    building_name TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    room_no INTEGER PRIMARY KEY AUTOINCREMENT,
    room_name TEXT NOT NULL,
    building_no INTEGER NOT NULL REFERENCES buildings(building_no) ON DELETE CASCADE
);

-- sqlite3 3.7.11+ added the standard syntax for adding multiple values
INSERT INTO buildings(building_name, address) VALUES ("ACME Headquaters", "3950 North 1st Street CA 95134");
INSERT INTO buildings(building_name, address) VALUES ("ACME Sales", "5000 North 1st Street CA 95134");

INSERT INTO rooms(room_name, building_no) VALUES ('Amazon', 1);
INSERT INTO rooms(room_name, building_no) VALUES ('War Room', 1);
INSERT INTO rooms(room_name, building_no) VALUES ('Office of CEO', 1);
INSERT INTO rooms(room_name, building_no) VALUES ('Marketing', 2);
INSERT INTO rooms(room_name, building_no) VALUES ('Showroom', 2);
