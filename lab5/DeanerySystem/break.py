from term import Term

class Break():

    def __init__(self, term: Term):
        self.term = term

        self.end = self.term.hour *60 + self.term.minute + self.term.duration
        self.end_hr = self.end // 60
        self.end_min = self.end % 60

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        info = f"{self.term.hour}:{self.term.minute} - {self.end_hr}:{self.end_min}"
        return info
