class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class SendmailHandler:

    def update(self, subject):
        from django.core.mail import send_mail

        print('Send Email!')
        send_mail('Print Ticket', 'Your ticket had been printed.', 'cs4125Amber@163.com', ['18111424@studentmail.ul.ie'])


#factory
class AdultTicketCreator(Subject):

    def print(self):
        return 'adult ticket'


class StudentTicketCreator(Subject):
    def print(self):
        return 'student ticket'


class ChildrenTicketCreator(Subject):
    def print(self):
        return 'children ticket'


def get_ticket_creator(type="Adult"):
    """Factory"""
    creators = {
        "Adult": AdultTicketCreator,
        "Student": StudentTicketCreator,
        "Children": ChildrenTicketCreator
    }

    return creators[type]()
