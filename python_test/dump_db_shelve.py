import shelve
db = shelve.open(
    r'F:\Repository\sshtest\python_test\people_data\people-shelve')
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
db.close()
