#!/usr/bin/env python

# Manipulate sys.path to be able to import converscript from this local git
# repository.
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from converscript import RiveScript
import json

bot = RiveScript()
bot.load_file("example.rive")

dep = bot.deparse()
print(json.dumps(dep, indent=2))
