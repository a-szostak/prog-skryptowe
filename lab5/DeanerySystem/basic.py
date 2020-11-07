

class BasicTerm:

    def __init__(self, hour, minute, duration = 90):
        self.__duration  = duration
        self.__minute = minute
        self.__hour = hour


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, var):
        self.__hour = var

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, var):
        self.__minute = var

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, var):
        self.__duration = var
