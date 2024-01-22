primes = []
verify = []
x = int(input("Enter starting range: "))
y = int (input("Enter terminal range: "))

        

for i in range(x, y+1):
    if i == 2:
        primes.append(i)
    print(i, end = ", ")
    if i > 2:
        for j in range(2, i+1):
            print(j, end=",, ")
            print(primes)
            if i % j == 0 and i != j:
                print("it")
                verify.append("a")
            elif i % j != 0:
                verify.append(j)
        if "a" in verify:
            verify.clear()
        elif "a" not in verify:
            primes.append(i)
            print("This is before: ", verify)
            verify.clear()
            print("This is verify: ", verify)
            print(primes)

print(primes)            
print(sum(primes))
