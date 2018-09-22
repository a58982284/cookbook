def checkio(*args):
    if not args:
        return 0
    else:
        return max(args) - min(args)
