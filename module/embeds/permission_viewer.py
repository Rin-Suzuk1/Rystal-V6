#  ------------------------------------------------------------
#  Copyright (c) 2024 Rystal-Team
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#  ------------------------------------------------------------
#

from nextcord.ui import View


def get_base_permissions(default_perm):
    """
    Retrieve the base permissions from the default permissions.

    Args:
        default_perm (dict): The default permissions dictionary.

    Returns:
        list: The base permissions list.
    """
    return list(default_perm.keys())


d = {
    "ping": "everyone",
    "info": "everyone",
    "bug": "everyone",
    "setting": {
        "game": {"game_announce_channel": "admin,mod"},
        "music": {
            "silent_mode": "admin,mod",
            "auto_leave": "admin,mod",
            "default_loop_mode": "admin,mod",
        },
        "language": "admin,mod",
    },
    "music": {
        "play": "everyone",
        "skip": "everyone",
        "queue": "everyone",
        "shuffle": "everyone",
        "loop": "everyone",
        "nowplaying": "everyone",
        "stop": "everyone",
        "pause": "everyone",
        "resume": "everyone",
        "remove": "everyone",
        "register": "everyone",
        "most_played": "everyone",
    },
    "rank": {"card": "everyone", "leaderboard": "everyone"},
    "point": {
        "claim": "everyone",
        "give": "everyone",
        "show": "everyone",
        "leaderboard": "everyone",
    },
    "permission": {"list": "admin,mod", "user": "admin", "role": "admin"},
    "note": {
        "create": "everyone",
        "list": "everyone",
        "view": "everyone",
        "remove": "everyone",
    },
    "shop": {"catalog": "everyone", "buy": "everyone"},
    "game": {
        "rules": {"jackpot": "everyone"},
        "jackpot": "everyone",
        "dice": "everyone",
        "roulette": "everyone",
        "coinflip": "everyone",
        "showjackpot": "everyone",
    },
}


class PermissionViewer(View):
    def __init__(
        self,
    ):
        super().__init__()
        raise NotImplementedError()
