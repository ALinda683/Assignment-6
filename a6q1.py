#Alinda Kumar Mazumder
#Student no. 11342454
#NSID: ugj683
#CMPT-145

def initialRead_state(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    initialState = [list(line.strip()) for line in lines]
    return initialState
