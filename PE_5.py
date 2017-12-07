#this program takes a number,n, and finds the smallest number that can be evenly devided by all the numbers between 1 and n inclusive
import numpy as np

def main():
  n = int(raw_input('Input an integer: '))
  base = prime_aggrigate(n)
  answer = factorizor(base,n)
  print(answer)

#takes in a top value and returns a list of all prime numbers in that range
def prime_aggrigate(top):
  primes = [2]
  for i in range(3,top):
    for prime in primes:
      if i%prime == 0:
        break
    else:
      primes.append(i)
  return primes

#this function takes in a list of prime numbers and the user specified integer and spits out the smallest number that is evenly devisable by every number in that range
def factorizor(nums, top):
  nums = np.array(nums)
  start = np.prod(nums)
  for j in range(4, top):
    if j not in nums and start%j != 0:#for all the numbers that aren't currently evenly devisable
      start *= int(1/((float(start)/j)%1))#multiply the base number by an amount needed to make it evenly devisable
  return start

main()
