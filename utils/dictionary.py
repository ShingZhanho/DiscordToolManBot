class Dictionary:
    def __init__(self, channel, command):
        if (command.replace('dict', '') == '') | (command.replace('dict', '') == ' '):
            self.status = '-1'  # -1 -> no word is passed in
            return

        self.word = command.replace('dict ', '')
        self.status = '0'

    def check_meaning(self):
        return f'指令：喺字典入面搵單字 \'{self.word}\''
