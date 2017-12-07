#Finds the difference between the sum of the squares of the first hundered numbers and the square of the sum

def main():
  celing = int(raw_input('Number to find sum square difference of: '))
  i = 1
  sum_of_sqrs = 0
  sqr_of_sums = 0
  while i <= celing:#cycle through specified numbers performing proper oporations
    sum_of_sqrs += i**2
    sqr_of_sums += i
    i += 1
  sqr_of_sums = sqr_of_sums**2
  print(sqr_of_sums-sum_of_sqrs)

main()
