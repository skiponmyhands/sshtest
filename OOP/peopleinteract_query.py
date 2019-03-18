# interactive queries
import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
#print(maxfield)
db = shelve.open(r'F:\Repository\sshtest\OOP\person_data\class-shelve')

while True:
    key = input('\nKey? => ')
    if not key:
        break
    try:
        record = db[key]
    except:
        print(f'No such key "{key}"!')
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))

