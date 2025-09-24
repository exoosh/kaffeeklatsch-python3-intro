print(f"top-level print in {__name__}  ({__file__=})")

__all__ = ["hello2"]


def hello2():
    print(f"Hello world from {__name__}.hello2()")


print(f"another top-level print in {__name__} ({__file__=})")
