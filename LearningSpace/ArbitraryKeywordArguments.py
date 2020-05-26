# def tag(name, **kwargs):
#     print(name)
#     print(kwargs)
#     print(type(kwargs))


def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}" '.format(k=key, v=str(value))
    result += '>'
    return result
