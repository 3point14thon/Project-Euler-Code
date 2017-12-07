#finds the product of a pythagorean triplet whoes sum is 1000

def main():
  total = 1000 #setting sum of a, b and c
  a = 2 #initializing
  b = 2.0
  c = (a**2+b**2)**(1/2.0)
  while a+b+c != total or c%1 != 0:#run while the sum isn't 'total' and c isn't an int
    a += 1
    b = 2.0
    while (a+b+c != total or c%1 != 0) and b != 300:
      b += 1 
      c = (a**2+b**2)**(1/2.0)
  print(int(a*b*c))

main()
