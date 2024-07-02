def is_simple_square(square):
    return square in [0, 1]

def dump(square):
    def _dump(square):
        if is_simple_square(square):
            print(square)
        else:
            for sub_square in square:
                _dump(sub_square)
    
    _dump(square)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; NICE JOB!\n")
