import sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from hanziconv import HanziConv

class VercaBOT:
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # 這個 ChatBot 的名字叫做 VercaBOT
        "VercaBOT",
        # 設定訓練的資料庫輸出於根目錄，並命名為 VercaBOT_DB.json
        database = "./VercaBOT_DB.json"
    )

    def __init__(self):
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)

        # self.chatbot.train("chatterbot.corpus.chinese")   
        self.chatbot.train("chatterbot.corpus.chinese.greetings")

    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

if __name__ == "__main__":
    bot = VercaBOT()
    result = str(bot.getResponse(sys.argv[1]))

    # 簡體轉繁體
    print(HanziConv.toTraditional(result))
