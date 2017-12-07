#takes in a top value and returns a list of all prime numbers in that range
def main():
  num = int(raw_input('nth prime number(input n): '))
  prime_aggrigate(num)
def prime_aggrigate(goal):
  primes = [2]
  i = 3
  while len(primes) < goal:#while the number of primes found is less than desired
    for prime in primes:#check if the i is devisable by any prime numbers
      if i%prime == 0:
        break
    else:
      primes.append(i)
    i += 1
  print(primes[-1])

main()
