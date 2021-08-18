import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFIle = open('errorInfo.txt', 'w')
    errorFIle.write(traceback.format_exc())
    errorFIle.close()
    print('The traceback info was written to errorInfo.txt')