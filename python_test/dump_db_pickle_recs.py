import pickle, glob
#a = glob.glob('./*.pkl')
#print(a)---['.\\bob.pkl', '.\\sue.pkl', '.\\tom.pkl']
for filename in glob.glob('./*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])