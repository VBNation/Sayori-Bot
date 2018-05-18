from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

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
    input_adapter="chatterbot_voice.VoiceInput",
    output_adapter="chatterbot_voice.VoiceOutput",
     database="D:\AI R+D\Sayori Bot\MK3\db.sqlite3"
)

bot.set_trainer(ChatterBotCorpusTrainer)

# Train the chat bot with the entire english corpus
#bot.train("chatterbot.corpus.english")

while True:
    try:
        # Use the parameter None because the VoiceInput adapter
        # is getting data from audio input instead of a parameter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
