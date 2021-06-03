def getChanges():
    changes = []
    try:
        with open('changes.txt', 'r+') as fp:
            content = fp.readlines()

        changes  = [i.split(" ") for i in content]
        
    except:
        changes = []

    
    return changes