from pycmmn.utils.StringUtil import StringUtil


def test_get_int():
    assert StringUtil.get_int("0") == 0
    assert StringUtil.get_int("10") == 10
    assert StringUtil.get_int("010") == 10

    assert StringUtil.get_int("-1") == -1
    assert StringUtil.get_int("0x010") == -1
    assert StringUtil.get_int("") == -1


def test_get_boolean():
    assert StringUtil.get_boolean("y") == True
    assert StringUtil.get_boolean("Y") == True
    assert StringUtil.get_boolean("true") == True
    assert StringUtil.get_boolean("True") == True
    assert StringUtil.get_boolean("tRUe") == True

    assert StringUtil.get_boolean("Yes") == False
    assert StringUtil.get_boolean("yes") == False
    assert StringUtil.get_boolean("예") == False
    assert StringUtil.get_boolean("no") == False
    assert StringUtil.get_boolean("#") == False
    assert StringUtil.get_boolean(".") == False
    assert StringUtil.get_boolean("") == False
