#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 # error because hidden_4 is in the /tmp directory

    for name in dir(hidden_4):
        if name[0:2] != "__":
            print("{}" .format(name))
