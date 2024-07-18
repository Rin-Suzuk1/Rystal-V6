#    ------------------------------------------------------------
#    Copyright (c) 2024 Rystal-Team
#  #
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#  #
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#  #
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#    THE SOFTWARE.
#    ------------------------------------------------------------
#  #

import json

from termcolor import colored

from .main_handler import cursor, database

default_user_data = {}


async def register_user(user_id: int):
    database.ping(reconnect=True, attempts=3)
    try:
        statement = "INSERT INTO note (user_id, notes) VALUES (%s, %s, %s)"
        values = (str(user_id), json.dumps(default_user_data))
        cursor.execute(statement, values)
        database.commit()
        print(
            colored(
                text=f"[NOTE DATABASE] Registered User: {user_id}", color="light_yellow"
            )
        )
    except Exception:
        print(
            colored(
                text=f"[NOTE DATABASE] Failed to Registered User: {user_id}",
                color="red",
            )
        )


async def add_note():
    uuid = str(uuid.uuid4())

    return
