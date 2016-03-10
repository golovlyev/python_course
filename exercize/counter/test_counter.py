# coding: utf-8

"""
    Test counter class
"""

from counter import Counter


def main():
    c = Counter()
    c.inc()
    c.inc()
    c.inc()
    c.inc()
    c.dec()
    c.dec()
    print(c.get())

    c = Counter(min_val=5, init_val=7)
    c.dec()
    c.dec()
    c.dec()
    c.dec()
    print(c.get())


if __name__ == '__main__':
    main()

