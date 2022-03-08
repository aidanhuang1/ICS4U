import glob

someList = glob.glob('eng*.csv')
#someList = glob.glob('*-1*.csv')

print(len(someList))
print(someList)
