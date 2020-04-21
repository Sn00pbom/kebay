def run(*args):
    import add
    o = 0
    for v in args:
        o = add.run(o, v)
    return o
        