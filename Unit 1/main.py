def fac(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * fac(n - 1)


n = int(input("Enter A Number"))
r = fac(n)
print(r)
