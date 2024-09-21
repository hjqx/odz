# func target
def x (obj):
    a,c=2,3
    b="hello,world!"
    return obj.__call__()

# retourne un dictionnaire des locals const et var d'une fonc
def mix (varnames : object, consts : object):
    return dict(zip(varnames.__code__.co_varnames,
        consts.__code__.co_consts))

d = (lambda e : mix(e,e))(x)

print(d["c"]) 
            # b var ignored cause he does not have const 
            # (('obj', 'a', 'c', 'b'), (None, (2, 3), 'hello,world!'))
            # so a : (2,3)  (counting as a tuple)
            #    c : 'hello,world' 
            #    indexing c and having "hello world" could be pretty confusing imo xD


# for tt in (lambda e : mix(e,e))(x).items() : 
#     print(tt)
