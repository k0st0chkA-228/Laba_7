import random
import string


class Password:
    def __init__(self):
        self.chrs = string.ascii_letters + string.digits
        self.ltrs = string.ascii_uppercase + string.ascii_lowercase
        self.psw = ""

    def gen_pas(self):
        self.psw = random.choice(self.ltrs) + random.choice(self.ltrs) + \
                   ''.join(random.choice(self.chrs) for i in range(4))

    def get_pas(self):
        return self.psw


p = Password()
k = 0
count = int(input('какое количество паролей нужно вывести?\n'))
for i in range(count):
    p.gen_pas()
    psw = p.get_pas()
    k += 1
    print(psw, '№', k)

