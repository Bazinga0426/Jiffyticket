#factory
class AdultTicketCreator:
    def print(self):
        return 'adult ticket'


class StudentTicketCreator:
    def print(self):
<<<<<<< HEAD
        return 'stuent ticket'
=======
        return 'student ticket'
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705


class ChildrenTicketCreator:
    def print(self):
        return 'children ticket'


def get_ticket_creator(type ="Adult"):
    """Factory"""
    creators = {
        "Adult": AdultTicketCreator,
        "Student": StudentTicketCreator,
        "Children": ChildrenTicketCreator
    }

    return creators[type]()
