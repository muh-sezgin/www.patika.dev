def flatten(unflatten):
    if not unflatten:
        return unflatten
    if isinstance(unflatten[0], list):
        return flatten(unflatten[0]) + flatten(unflatten[1:])
    return unflatten[:1] + flatten(unflatten[1:])