# -*- coding: utf-8 -*-

from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
#import logging
#logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot

bot = ChatBot(
    "Sayori",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.90,
            'default_response': 'I am sorry, but I do not understand.'
        },
        "chatterbot.logic.MathematicalEvaluation",
        #"chatterbot.logic.TimeLogicAdapter",
        
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="D:\AI R+D\Sayori Bot\MK3\db.sqlite3"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
