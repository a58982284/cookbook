'''
如果密码的长度大于或等于10个字符，且其中至少有一个数字、一个大写字母和一个小写字母，
该密码将被视为足够强大。密码只包含ASCII拉丁字母或数字
re.match("[a-zA-Z0-9]+", password)
9 < len(password) ≤ 64
'''
import re


def password(password):
    if re.match("[a-zA-Z0-9]+", password) and 9 < len(password) <= 64:
        return True
    else:
        return False
if __name__ == '__main__':
    print (password("QwErTy911poqqqq"))
    print (password('A1213pokl'))
    print (password('bAse730onE4'))

DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')


def checkio(data):
    """
    Return True if password strong and False if not

    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False

    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False

    return True