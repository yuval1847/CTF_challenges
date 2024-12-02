import sqlite3
conn = sqlite3.connect("C:\\Users\\USER\\Desktop\\CTF_challenges\\Programming_Club_BlackBoxes\\BlackBox7\\challenge\\game_database.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO users VALUES ('1', 'yuyu', '1847')")
conn.commit()
conn.close()