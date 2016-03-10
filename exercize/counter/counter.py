# coding: utf-8

"""
    Simple counter classes
"""


class Counter(object):
    __value = 0
    __min = 0
    __max = 0

    def __init__(self, min_val=0, max_val=10, init_val=0):
        self.__min = min_val
        self.__max = max_val
        self.__value = init_val

    def inc(self):
        if self.__value < self.__max:
            self.__value += 1

    def dec(self):
        if self.__value > self.__min:
            self.__value -= 1

    def get(self):
        return self.__value