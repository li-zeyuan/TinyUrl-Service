CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def convert_to_62system(num):
    """
    将数字转化成62进制
    :param num: 十进制数字(int)
    :return: 62进制字符串(str)
    """
    if num == 0:
        return CHARS[0]

    res = []
    while num:
        num, rem = divmod(num, len(CHARS))  # num为商, rem为余数
        res.append(CHARS[rem])
    return "".join(reversed(res))


if __name__ == '__main__':
    print(convert_to_62system(1))
    print(convert_to_62system(61))
