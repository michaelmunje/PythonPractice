import re


def is_non_empty(lst):
    if len(lst) > 0:
        return True
    else:
        return False


def test_re():
    a_or_b = re.compile(r'[^ab]+')
    assert is_non_empty(a_or_b.findall("abcba")) is True
    assert is_non_empty(a_or_b.findall("abbbb")) is False


if __name__ == "__main__":
    test_re()
