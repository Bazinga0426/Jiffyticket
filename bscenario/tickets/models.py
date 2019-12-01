#factory
class AdultTicketCreator:
    def print(self):
        return 'adult ticket'


class StudentTicketCreator:
    def print(self):
        return 'stuent ticket'


class ChildrenTicketCreator:
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
