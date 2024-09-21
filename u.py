def x (obj):
    a,c=2,3
    r,x=0,1
    return obj.__call__()
def mix (varnames : object, consts : object):
    return dict(zip(varnames.__code__.co_varnames,
        consts.__code__.co_consts))

d = (lambda e : mix(e,e))(x)
print(d["c"]) # 0,1
