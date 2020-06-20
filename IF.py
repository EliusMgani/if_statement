n=int(input().strip())
check={True: "Not Weird", False: "Weird"}

print(check[
    n%2==20 and (
        n in range (2,6) or
        n > 20)
    ])
