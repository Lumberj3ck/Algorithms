#!/usr/bin/env python3


def main():
    global g
    g = 9999
    f = 5
    def nested():
        global f
        f = 1
    nested()
    print(f)

main()
print(g)
print(f)
