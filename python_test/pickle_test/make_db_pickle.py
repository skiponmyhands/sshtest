from initdata import db
import pickle

dbfile = open(r'F:\Repository\sshtest\python_test\people_data\people-pickle', 'wb')    # 使用3.*的二进制模式文件
pickle.dump(db, dbfile)                 # 字节数据，而非字符串
dbfile.close()
