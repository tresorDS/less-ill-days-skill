from mycroft import MycroftSkill, intent_file_handler


class LessIllDays(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('days.ill.less.intent')
    def handle_days_ill_less(self, message):
        self.speak_dialog('days.ill.less')


def create_skill():
    return LessIllDays()

