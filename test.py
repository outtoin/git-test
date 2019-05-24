from socket import *

def function1():
    print('this is function 1')

if __name__ == "__main__":
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('0.0.0.0', 0))

    while True:
        data, addr = s.recvfrom(1024)
        print(data, addr)
    