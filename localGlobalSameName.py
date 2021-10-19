def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'spam local'
    spam()  
    print(eggs) # prints 'spam local'

eggs = 'global'
bacon()
print(eggs) # print 'global'
