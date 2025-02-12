class email:
    def send(self):
        print('email sent')
class sms:
    def send(self):
        print('sms received')
class push:
    def send(self):
        print('push ')

def notif(obj):
    
    obj.send()

e=email()
notif(e)
s=sms()
notif(s)
p=push()
notif(p)
    
    
