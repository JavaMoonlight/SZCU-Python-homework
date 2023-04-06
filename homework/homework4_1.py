# Calculate Bezu's theorem
def ged(p,q):
    d = calculate(p,q)
    x,y,num1,num2 = 0,1,1,0
    while q!=0:
        number = p // q
        p,q = q,p%q
        x,num1 = num1-number * x,x
        y,num2 = num2-number * y,y
    result = (d,num1,num2)
    return result

# Calculate the greatest common divisor
def calculate(p,q):
    m = max(p, q)
    n = min(p, q)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

# Main running function
def main():
    print("please enter two numbers:")
    num1 = int(input())
    num2 = int(input())
    if num1 < 0 or num2 < 0:
        print("please enter again")
    else:
        result = ged(num1, num2)
        print(result)

main()