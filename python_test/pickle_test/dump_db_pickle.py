import pickle
dbfile = open(r'F:\Repository\sshtest\python_test\people_data\people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
