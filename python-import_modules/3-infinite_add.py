#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0")
    else:
        total_sum = 0
        for i in range(1, argc + 1):
            total_sum = total_sum + int(argv[i])
        print(total_sum)
