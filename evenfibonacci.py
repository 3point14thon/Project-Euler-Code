#Prints the sum of all of the even members of fibonacci's sequence under four million

def main():
  hold = 0
  fib1 = 1
  fib2 = 2
  total = 0
  while fib2 < 4000000:
    hold = fib1 + fib2
    fib1 = fib2
    fib2 = hold
    if fib2 % 2 == 0:
      total += fib2
  print total
main()
