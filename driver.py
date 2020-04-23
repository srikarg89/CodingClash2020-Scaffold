from RestrictedPython import compile_restricted

import sys
import os
import ast

board_size = 30
board = [[None]*board_size]*board_size
team1 = sys.argv[1]
team2 = sys.argv[2]

byte_code = compile_restricted("", filename='example_bot/bot.py', mode='exec')
