print(f"top-level print in {__name__}  ({__file__=})")

__all__ = ["hello"]


def hello():
    print(f"Hello world from {__name__}.hello()")


print(f"another top-level print in {__name__} ({__file__=})")
