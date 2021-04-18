def sequential_search(seq, n):
    for item in seq:
        if item == n:
            return True
    return False


def test_sequential_search():
    seq = [1, 5, 6, 9, 3]
    target1 = 5
    target2 = 7
    assert(sequential_search(seq, target1) == True)
    assert(sequential_search(seq, target2) == False)
    print('테스트 통과!')


if __name__ == "__main__":
    test_sequential_search()
