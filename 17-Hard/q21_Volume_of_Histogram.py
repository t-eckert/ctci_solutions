'''
  17.21 Volume of Histogram: Design an algorithm to compute the colume of water it could hold if someone poured water across the top. Each histogram bar has a width of 1.
'''

test_hist = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 6, 0, 1]

def fill_hist(hist):
  zeroes = [0]
  z_indx = 0
  l_bounds = []
  pool_sizes = []
  for r_bound in hist:
    if r_bound == 0 and l_bounds != []:
      zeroes[z_indx] += 1
    elif r_bound != 0:
      if l_bounds == []:
        l_bounds.append(r_bound)
      else:
        for i in range(len(l_bounds)):
          if l_bounds[-1-i] < r_bound:
            pool_sizes.append((l_bounds[-1-i]-sum(l_bounds[len(l_bounds)-i:]))*(sum(zeroes[z_indx-i:z_indx+1])+i))
          if l_bounds[-1-i] == r_bound:
            pool_sizes.append((l_bounds[-1-i]-sum(l_bounds[len(l_bounds)-i:]))*(sum(zeroes[z_indx-i:z_indx+1])+i))
            break
          if l_bounds[-1-i] > r_bound:
            pool_sizes.append((r_bound -sum(l_bounds[len(l_bounds)-i:]))*(sum(zeroes[z_indx-i:z_indx+1])+i))
            break
        l_bounds.append(r_bound)
        zeroes.append(0)
        z_indx += 1
    print("r_bound: %s \nl_bounds: %s \nzeroes: %s \npool_sizes: %s \n" % (r_bound, l_bounds, zeroes, pool_sizes))
  return pool_sizes

def main():
  print(fill_hist(test_hist))
  pass

main()