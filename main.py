# Author: Dymea Schippers dxs5940@psu.edu
# Collaborator: Olivia Mandola ovm5126@psu.edu
# Collaborator: Michael Sullivan mls6888@psu.edu
# Section: 11R
# Breakout: 11

def sum_n(n):
  if (n <= 0):
    return 0
  else:
    return n+sum_n(n-1)

def print_n(s, n):
  if (n != 0):
    print(s)
    print_n(s, n - 1)
  
def run():
  n = int(input("Enter an int: "))
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print_n(s, n)

if __name__ == "__main__":
  run()

