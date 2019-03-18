from person import Person


class Mannager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
#        self.pay *= (1+percent+bonus)

# code for testing
if __name__ == '__main__':
    tom = Mannager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(0.2)
    print(tom.pay)
