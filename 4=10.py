#problem: give n numbers, what combination of + - * / and () makes x

from itertools import permutations, product, zip_longest
from pars import genPars

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

    parList = genPars(len(nums))

    finalP = []

    for f in finalList:
        finalP.append(f)
        for p in parList:
            x = f[:]
            if len(p) != 2:
                raise Exception("ERROR incorrect number of parentheses")
            x.insert(p[0],'(')
            x.insert(p[1],')')
            finalP.append(x)

    #compress the list of lists into a list of strings
    final = [''.join(str(element) for element in f) for f in finalP]

    return final


def calculate(final,x):
    results = {}
    for f in final:
        try:
            results[f] = eval(f)
            if results[f] == x:
                print(results[f])
                break
        except ZeroDivisionError:
            continue
        
    #TO DO 
    #Prune equal solutions
    
    for key,val in results.items():
        if val == 10:
            print(key,val)
            break

    print("No Solution")
        
def main():

    allnums = [ [i,j,k,l] for i in range(10) for j in range(10) for k in range(10) for l in range(10)]

    for a in allnums:
        print(a)
        final = genAll(a)    
        calculate(final,10)

    #nums = [9,8,7,6]

    #final = genAll(nums)    
    #calculate(final,10)

if __name__ == "__main__":
    main()
    