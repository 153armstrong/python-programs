# I was facinated by the pascal's triangle and wanted to play around with it.. I wanted to test out a few things on the larger scale
# and foudn this code online at http://stackoverflow.com/questions/24093387/pascals-triangle-for-python
# Made a few changes and it now prints it beautifully 

import math,sys

# pascals_tri_formula = [] # don't collect in a global variable.

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing 
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append((combination(count, element))%7)
        result.append(row)
        # count += 1 # avoidable
    return result

# now we can print a result:
count = 50 ## Prints for 50 rows 
for row in pascals_triangle(50):
    sys.stdout.write(" "*count)
    for i in row:
        sys.stdout.write(str(i) + " ")
    sys.stdout.write("\n")
    count-=1
    
    
## OUTPUT FROM THE PROGRAM 

                                                  1 
                                                 1 1 
                                                1 2 1 
                                               1 3 3 1 
                                              1 4 6 4 1 
                                             1 5 3 3 5 1 
                                            1 6 1 6 1 6 1 
                                           1 0 0 0 0 0 0 1 
                                          1 1 0 0 0 0 0 1 1 
                                         1 2 1 0 0 0 0 1 2 1 
                                        1 3 3 1 0 0 0 1 3 3 1 
                                       1 4 6 4 1 0 0 1 4 6 4 1 
                                      1 5 3 3 5 1 0 1 5 3 3 5 1 
                                     1 6 1 6 1 6 1 1 6 1 6 1 6 1 
                                    1 0 0 0 0 0 0 2 0 0 0 0 0 0 1 
                                   1 1 0 0 0 0 0 2 2 0 0 0 0 0 1 1 
                                  1 2 1 0 0 0 0 2 4 2 0 0 0 0 1 2 1 
                                 1 3 3 1 0 0 0 2 6 6 2 0 0 0 1 3 3 1 
                                1 4 6 4 1 0 0 2 1 5 1 2 0 0 1 4 6 4 1 
                               1 5 3 3 5 1 0 2 3 6 6 3 2 0 1 5 3 3 5 1 
                              1 6 1 6 1 6 1 2 5 2 5 2 5 2 1 6 1 6 1 6 1 
                             1 0 0 0 0 0 0 3 0 0 0 0 0 0 3 0 0 0 0 0 0 1 
                            1 1 0 0 0 0 0 3 3 0 0 0 0 0 3 3 0 0 0 0 0 1 1 
                           1 2 1 0 0 0 0 3 6 3 0 0 0 0 3 6 3 0 0 0 0 1 2 1 
                          1 3 3 1 0 0 0 3 2 2 3 0 0 0 3 2 2 3 0 0 0 1 3 3 1 
                         1 4 6 4 1 0 0 3 5 4 5 3 0 0 3 5 4 5 3 0 0 1 4 6 4 1 
                        1 5 3 3 5 1 0 3 1 2 2 1 3 0 3 1 2 2 1 3 0 1 5 3 3 5 1 
                       1 6 1 6 1 6 1 3 4 3 4 3 4 3 3 4 3 4 3 4 3 1 6 1 6 1 6 1 
                      1 0 0 0 0 0 0 4 0 0 0 0 0 0 6 0 0 0 0 0 0 4 0 0 0 0 0 0 1 
                     1 1 0 0 0 0 0 4 4 0 0 0 0 0 6 6 0 0 0 0 0 4 4 0 0 0 0 0 1 1 
                    1 2 1 0 0 0 0 4 1 4 0 0 0 0 6 5 6 0 0 0 0 4 1 4 0 0 0 0 1 2 1 
                   1 3 3 1 0 0 0 4 5 5 4 0 0 0 6 4 4 6 0 0 0 4 5 5 4 0 0 0 1 3 3 1 
                  1 4 6 4 1 0 0 4 2 3 2 4 0 0 6 3 1 3 6 0 0 4 2 3 2 4 0 0 1 4 6 4 1 
                 1 5 3 3 5 1 0 4 6 5 5 6 4 0 6 2 4 4 2 6 0 4 6 5 5 6 4 0 1 5 3 3 5 1 
                1 6 1 6 1 6 1 4 3 4 3 4 3 4 6 1 6 1 6 1 6 4 3 4 3 4 3 4 1 6 1 6 1 6 1 
               1 0 0 0 0 0 0 5 0 0 0 0 0 0 3 0 0 0 0 0 0 3 0 0 0 0 0 0 5 0 0 0 0 0 0 1 
              1 1 0 0 0 0 0 5 5 0 0 0 0 0 3 3 0 0 0 0 0 3 3 0 0 0 0 0 5 5 0 0 0 0 0 1 1 
             1 2 1 0 0 0 0 5 3 5 0 0 0 0 3 6 3 0 0 0 0 3 6 3 0 0 0 0 5 3 5 0 0 0 0 1 2 1 
            1 3 3 1 0 0 0 5 1 1 5 0 0 0 3 2 2 3 0 0 0 3 2 2 3 0 0 0 5 1 1 5 0 0 0 1 3 3 1 
           1 4 6 4 1 0 0 5 6 2 6 5 0 0 3 5 4 5 3 0 0 3 5 4 5 3 0 0 5 6 2 6 5 0 0 1 4 6 4 1 
          1 5 3 3 5 1 0 5 4 1 1 4 5 0 3 1 2 2 1 3 0 3 1 2 2 1 3 0 5 4 1 1 4 5 0 1 5 3 3 5 1 
         1 6 1 6 1 6 1 5 2 5 2 5 2 5 3 4 3 4 3 4 3 3 4 3 4 3 4 3 5 2 5 2 5 2 5 1 6 1 6 1 6 1 
        1 0 0 0 0 0 0 6 0 0 0 0 0 0 1 0 0 0 0 0 0 6 0 0 0 0 0 0 1 0 0 0 0 0 0 6 0 0 0 0 0 0 1 
       1 1 0 0 0 0 0 6 6 0 0 0 0 0 1 1 0 0 0 0 0 6 6 0 0 0 0 0 1 1 0 0 0 0 0 6 6 0 0 0 0 0 1 1 
      1 2 1 0 0 0 0 6 5 6 0 0 0 0 1 2 1 0 0 0 0 6 5 6 0 0 0 0 1 2 1 0 0 0 0 6 5 6 0 0 0 0 1 2 1 
     1 3 3 1 0 0 0 6 4 4 6 0 0 0 1 3 3 1 0 0 0 6 4 4 6 0 0 0 1 3 3 1 0 0 0 6 4 4 6 0 0 0 1 3 3 1 
    1 4 6 4 1 0 0 6 3 1 3 6 0 0 1 4 6 4 1 0 0 6 3 1 3 6 0 0 1 4 6 4 1 0 0 6 3 1 3 6 0 0 1 4 6 4 1 
   1 5 3 3 5 1 0 6 2 4 4 2 6 0 1 5 3 3 5 1 0 6 2 4 4 2 6 0 1 5 3 3 5 1 0 6 2 4 4 2 6 0 1 5 3 3 5 1 
  1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
