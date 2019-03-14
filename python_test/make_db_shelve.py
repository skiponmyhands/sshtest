from initdata import bob, sue
import shelve
db = shelve.open(
    r'F:\Repository\sshtest\python_test\people_data\people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
