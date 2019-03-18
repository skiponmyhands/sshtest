import shelve
with shelve.open(r'F:\Repository\sshtest\OOP\person_data\class-shelve') as db:
    for key in db:
        print(key, '=>\n ', db[key].name, db[key].pay)