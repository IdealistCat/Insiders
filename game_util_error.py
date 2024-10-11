# Insider Error Handler

def throwError(error, file):
    raise Exception(errorstring(error, file))

def passError(error, file):
    print(errorstring(error, file))

def errorstring(err, fi):
    return f"\nError from {fi}.py: {err}"