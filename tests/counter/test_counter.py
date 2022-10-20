from src.counter import count_ocurrences


def test_counter():
    count = count_ocurrences("tests/mocks/jobs.csv", "developer")
    print(count)
    assert count == 3
