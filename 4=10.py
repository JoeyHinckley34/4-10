#problem: give n numbers, what combination of + - * / makes x
#inspiration 4=10 game.
#This problem done in HTML, CSS, and Javascript: https://eigilnikolajsen.dk/4is10-solver/

from itertools import permutations, product, zip_longest, combinations
 
def genAll(nums):
    # Get all permutations of nums
    perm = list(permutations(nums))
    ops = ['+','-','/','*']
    allOps = product(ops, repeat = len(nums)-1)

    finalList = []
    finIter = 0

    for o in allOps:
        for p in perm:
            #print(p)
            finalList.append([])
            for x,y in zip_longest(p,o):
                
                finalList[finIter].append(x)

                if y is not None:
                    finalList[finIter].append(y)

            finIter += 1

    
    #compress the list of lists into a list of strings
    final = [''.join(str(element) for element in f) for f in finalList]



    pars = [0,2,4,6]
    p = combinations(pars,2)
  
    for i, x in enumerate(p):
        print(i,x)
    
    # for f in final:
    #     print(f)





    return final

def calculate(final,x):
    results = {}
    for f in final:
        try:
            results[f] = eval(f)
        except ZeroDivisionError:
            continue
        
    for key,val in results.items():
        if val == 10:
            print(key,val)


def main():
    nums = [4,4,3,8]

    final = genAll(nums)    
    calculate(final,10)

if __name__ == "__main__":
    main()
    