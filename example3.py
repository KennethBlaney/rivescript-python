#!/usr/bin/python3

# Python 3 example

from converscript import ConverScript

cs = ConverScript()
cs.load_directory("./eg/brain")
cs.sort_replies()

print("""This is a bare minimal example for how to write your own RiveScript bot!

For a more full-fledged example, try running: `python converscript brain`
This will run the built-in Interactive Mode of the RiveScript library. It has
some more advanced features like supporting JSON for communication with the
bot. See `python converscript --help` for more info.

example3.py is just a simple script that loads the RiveScript documents from
the 'brain/' folder, and lets you chat with the bot.

Type /quit when you're done to exit this example.
""")

while True:
    msg = input("You> ")
    if msg == '/quit':
        quit()
    reply = cs.reply("localuser", msg)
    print("Bot>", reply)

# vim:expandtab
