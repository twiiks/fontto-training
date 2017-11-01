import os
from slackclient import SlackClient


class slackbot:

    def __init__(self, token=-1):
        if token == -1:
            slack_token = os.environ["SLACK_TOKEN_TRAINING"]
        else:
            slack_token = token
        self.sc = SlackClient(slack_token)

    def sendMessage(self, channel, text):
        self.sc.api_call("chat.postMessage", channel=channel, text=text)

    def sendToTraining(self, text):
        self.sendMessage("#training", text)

    def trainingBegin(self, data_name, total_epoch, saving_epoch):
        # 이름, 총에폭, 얼마마다 알려줄 것인지
        text = \
'''----------------------------------새로운 학습이 시작됐어요----------------------------------
학습할 data 이름은 [%s]
총 epoch은 [%d]
입니다.

그럼 [%d] 에폭마다 알려드릴게요!''' % (data_name, total_epoch, saving_epoch)
        # print(text)
        self.sendToTraining(text)

    def trainingProgress(self, data_name, epoch, time_taken):
        text = \
'''        [%s]
        진행 에폭 : [%d]
        지금까지 걸린 시간 : [%s]
''' % (data_name, epoch, time_taken)
        self.sendToTraining(text)

    def trainingDone(self, data_name, total_epoch, time_taken):
        text = \
'''        [%s]
        진행 에폭 : [%d]
        총 걸린 시간 : [%s]
----------------------------------학습이 끝났습니다----------------------------------
''' % (data_name, total_epoch, time_taken)
        self.sendToTraining(text)
