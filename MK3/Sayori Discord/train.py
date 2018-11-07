# -*- coding: utf-8 -*-

from chatterbot import ChatBot


from chatterbot.trainers import *

chatterbot = ChatBot("Sayori")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english"
)
