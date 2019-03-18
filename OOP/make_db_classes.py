import shelve
from person import Person
from manager import Mannager


bob = Person('Bob Smith', 44, 30000, 'software')
sue = Person('Sue Jones', 47, 40000, 'Hardware')
tom = Person('Tom Doe', age=50, pay=50000)

db = shelve.open(r'F:\Repository\sshtest\OOP\person_data\class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
