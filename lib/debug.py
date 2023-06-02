#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':

 class Song:
   def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
    
   @classmethod
   def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
   def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
   @classmethod
   def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

def reset_database():
    Song.drop_table()
    Song.create_table()
    Song.create("Hello", "25")
    Song.create("99 Problems", "The Black Album")


reset_database()
   
import ipdb; ipdb.set_trace()
