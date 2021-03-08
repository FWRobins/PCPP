class time_interval():
    def __init__(self, hours=0, minutes=0, seconds=0):
        if type(hours)==int and type(minutes)==int and type(seconds)==int:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.total_seconds = hours*60*60+minutes*60+seconds
        else:
            raise TypeError

    def to_string(self, seconds):
        hours = seconds//(60*60)
        minutes = (seconds-(hours*60*60))//60
        seconds = seconds%60
        return str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)

    def __str__(self):
        return self.to_string(self.total_seconds)

    def __add__(self, other):
        if type(other) == int:
            other = time_interval(seconds=other)
            return self.to_string(self.total_seconds+other.total_seconds)
        else:
            return self.to_string(self.total_seconds+other.total_seconds)

    def __sub__(self, other):
        if type(other) == int:
            other = time_interval(seconds=other)
            return self.to_string(self.total_seconds-other.total_seconds)
        else:
            return self.to_string(self.total_seconds-other.total_seconds)

    def __mul__(self, value):
        return self.to_string(self.total_seconds*value)

time1 = time_interval(21,58,50)
time2 = time_interval(1, 45, 22)
print(time1+time2)
print(time1-time2)
print(time1*2)
print(time1+5)
print(time2-5)
