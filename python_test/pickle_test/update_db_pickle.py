import pickle
dbfile = open(r'F:\Repository\sshtest\python_test\people_data\people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open(r'F:\Repository\sshtest\python_test\people_data\people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
