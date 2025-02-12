from abc import ABC,abstractmethod
class Notify(ABC):
    def notification(self):
        print('notifications')
    @abstractmethod
    def send(self):
        pass
class Email(Notify):
    def send(self):
        print('email sent')
class SMS(Notify):
    def send(self):
        print('SMS sent')
class Push(Notify):
    def send(self):
        print('push 2 start')   

c=Email()
c.notification()
c.send()
s=SMS()
s.send()
p=Push()
p.send()
