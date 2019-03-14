from initdata import tom
import shelve
db = shelve.open(
    r'F:\Repository\sshtest\python_test\people_data\people-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
db['tom'] = tom
db.close()
