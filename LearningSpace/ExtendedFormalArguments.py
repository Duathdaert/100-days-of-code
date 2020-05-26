# Extended Formal Arguments learning


def hypervolume(length, *lengths):
    v = length
    for part in lengths:
        v *= part
    return v