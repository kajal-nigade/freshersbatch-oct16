def listToString(list):
    if list[-1]:
        list.append('and '+str(list[-1]))
        list.remove(list[-2])
    for i in range(len(list)):
        print(''+list[i]+', ')

spam = ['apples', 'bananas', 'tofu', 'cats']


listToString(spam)