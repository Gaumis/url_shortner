BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num: int) -> str:
    if num == 0:
        return BASE62[0]

    base = len(BASE62)
    result = []

    while num:
        num, rem = divmod(num, base)
        result.append(BASE62[rem])

    return ''.join(reversed(result))