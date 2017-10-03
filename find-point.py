def find_point():
    tc = input()
    while tc > 0:
        arr = map(int, raw_input().strip().split(' '))
        print (arr[2] + (arr[2] - arr[0])), (arr[3] + (arr[3] - arr[1]))
        tc -= 1

def main():
    find_point()

if __name__ == "__main__":
    main()