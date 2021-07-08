# door mat
import math

n,m = input().split()

def gen_mat(n, m):
    if (int(n) != int(m) / 3):
      print("Please enter value of N equals to one third of M")
    else:
        n = int(n)
        m = int(m)

        # Top pattern
        for i in range(0, math.floor(n/2)):
            print(("-" * (math.floor(m/2) - 1 - 3 * i)) + (".|." * (2*i + 1)) + ("-" * (math.floor(m/2) - 1 - 3 * i)))

        # Middle line with WELCOME
        print("-" * (math.floor(m/2) - 3) + "WELCOME" + "-" * (math.floor(m/2) - 3))

        # Bottom pattern
        for i in range(math.floor(n/2) - 1, -1, -1):
            print(("-" * (math.floor(m/2) - 1 - 3 * i)) + (".|." * (2*i + 1)) + ("-" * (math.floor(m/2) - 1 - 3 * i)))

gen_mat(n,m)
    



