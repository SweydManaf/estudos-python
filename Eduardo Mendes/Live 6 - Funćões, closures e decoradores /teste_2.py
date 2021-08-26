from pdb import set_trace

var = 7

def func():
    # set_trace()
    global var
    print(var)
    var = 18
    print(var)

func()
print(var)