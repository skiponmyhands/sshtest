# 交互式更新
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open(r'F:\Repository\sshtest\OOP\person_data\class-shelve')
while True:
    key = input('\nKey? => ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input(f'\t[{field}] = {currval}\n\t\tnew?=>')
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
