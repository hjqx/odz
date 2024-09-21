# func targzet
def x (obj):
    a=2
    b="hello,world!"
    return obj.__call__()

# retourne une list[tuple] des locals const et var d'une fonc
def mix (varnames : object, consts : object):
    return list(zip(varnames.__code__.co_varnames,
        consts.__code__.co_consts))

for tt in (lambda e : mix(e,e))(x) : #peut etre très utile pour mes obfs
    print(tt)
