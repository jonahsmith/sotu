#!/usr/bin/python

import sys

def main():

    with open("5050.txt") as f:
        contents = f.read()
        address = []
        for entry in contents.split("***"):
            address.append(entry)

    for i in range(6):
        address.pop(0)

    for i in range(6):
        address.pop(len(address)-1)

    searchTerm = sys.argv[1].lower()
    for i in range(len(address)):
        thisAddress = address[i].lower()
        if searchTerm in thisAddress:
            addressLines=address[i].split('\n')
            print(addressLines[3]+" (" + addressLines[4] + ")")

if __name__ == '__main__':
    main()
