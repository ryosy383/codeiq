#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def counter():
    count = 0
    def nested():
        nonlocal count
        count += 1
        print(count)
    return nested
c1 = counter()
c2 = counter()
c1()
c2()
c2()
c1()

