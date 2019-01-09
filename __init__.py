from mycroft import MycroftSkill, intent_file_handler


class Aravind(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('aravind.intent')
    def handle_aravind(self, message):
        self.speak_dialog('aravind')


def create_skill():
    return Aravind()

