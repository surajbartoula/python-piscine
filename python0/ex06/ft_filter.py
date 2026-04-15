def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the item that are true.
    """
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])


def main():
    """
    Empty main function to satisfy the project requirement
    without exectuting additional test logic
    """
    pass


if __name__ == "__main__":
    main()
