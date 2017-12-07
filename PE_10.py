#finds the sum of all prime numbers below the input
import numpy as np

def main():
  num = int(raw_input('sum of primes below: '))
  prime_aggrigate(num)
def prime_aggrigate(goal):
  primes = [2]
  i = 3
  while i < goal:#while the number i is less than desired
    for prime in primes:#check if the i is devisable by any prime numbers
      if i%prime == 0:
        break
    else:
      primes.append(i)
    i += 1
    print(i)
  primes = np.array(primes)
  print(np.sum(primes))

main()
