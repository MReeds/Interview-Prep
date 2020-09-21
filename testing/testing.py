# An integration test checks that components in your application operate with each other.
# A unit test checks a small component in your application.

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
