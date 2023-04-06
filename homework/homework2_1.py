def dragon(f,l,r,n):
    if n<5:
        if n == 0:
            print(f)
        elif n == 1:
            print(f+l)
        else:
            l += l;
            l += r;
            print(f + l)
        n += 1
        dragon(f,l,r,n)

def main():
    level = 0
    f = "F"
    l = "LF"
    r = "RF"
    dragon(f,l,r,level)
main()