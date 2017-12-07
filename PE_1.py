#prints the sum of all the multiples of three and five below 1000

def main():
  threes = summult(3)
  fives = summult(5)
  print threes + fives

def summult(n):
  cutoff = (1000-1)//n
  return n*cutoff*(cutoff-1)/2

main()
