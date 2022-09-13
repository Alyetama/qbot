#!/usr/bin/env python
# coding: utf-8

import hashlib
import random
import sqlite3
from datetime import datetime
from typing import Tuple, Union, Optional


class Database:

    def __init__(self, db_file: str = 'qbot_db.db'):
        self.con = sqlite3.connect(db_file, isolation_level=None)
        self.cur = self.con.cursor()

    def start(self) -> None:
        try:
            self.cur.execute('''CREATE TABLE quotes(
                id INTEGER PRIMARY KEY,
                keyword TEXT NOT NULL,
                message TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                created_on TEXT NOT NULL,
                md5_checksum TEXT NOT NULL
            );''')
        except sqlite3.OperationalError:
            pass

    def insert_quote(self, keyword: str, message: str,
                     user_id: int) -> Tuple[Union[bool, str], Optional[tuple]]:

        md5_checksum = hashlib.md5(message.encode()).hexdigest()
        exists = self.cur.execute(
            '''SELECT id, user_id, md5_checksum
            FROM quotes
            WHERE user_id=? AND md5_checksum=?''',
            (user_id, md5_checksum)).fetchone()

        if exists:
            return exists, None

        created_on = str(datetime.now())
        _id = self.cur.execute(
            'SELECT id FROM quotes ORDER BY id DESC LIMIT 1').fetchone()
        if not _id:
            _id = 0
        else:
            _id = _id[0] + 1

        values = (_id, keyword, message, user_id, created_on, md5_checksum)
        self.cur.execute('INSERT INTO quotes VALUES (?, ?, ?, ?, ?, ?)',
                         values)
        return False, values

    def fetch_quote(self, keyword: str) -> tuple:
        quotes = self.cur.execute(
            'SELECT id, message FROM quotes WHERE keyword=?',
            (keyword, )).fetchall()
        return random.choice(quotes)

    def delete_quote(self, _id: int, user_id: int) -> None:
        self.cur.execute('DELETE FROM quotes WHERE id=? AND user_id=?',
                         (_id, user_id))

    def fetch_by_id(self, _id: int) -> tuple:
        return self.cur.execute(
            '''SELECT id, user_id, keyword, message, created_on
            FROM quotes WHERE id=?''', (_id, )).fetchone()

    def fetch_random_quote(self) -> tuple:
        quotes = self.cur.execute(
            'SELECT id, message FROM quotes').fetchall()
        if quotes:
            return random.choice(quotes)
