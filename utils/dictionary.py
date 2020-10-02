class Dictionary:
    def __init__(self, word: str):
        self.word = word

    def check_meaning(self):
        return f'指令：喺字典入面搵單字 \'{self.word}\''
