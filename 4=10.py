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
    
    p = False

    for f in final:
        try:
            results[f] = eval(f)
            if results[f] == x:
                print(f,'=',results[f])
                p = True
                break
        except ZeroDivisionError:
            continue
        
    #TO DO 
    #Prune equal solutions
   

    # for key,val in results.items():
    #     if val == 10:
    #         print(key,val)
    #         p = True
    #         break

    if not p:
        print("No Solution ",final[0].split("+"))
        
#@param n : desired size of list
#@param m : range
#@returns allnums : a list of list constisting of all possible ways to arrange n numbers in the range 0-m without duplicates
def generate_allnums(n, m):
    return set([tuple(sorted(combination)) for combination in product(range(m), repeat = n)])

def main():
    allnums = generate_allnums(4, 10)


    #allnums = genAllNums(4,10)
    # print(allnums)
    # for a in allnums:
    #     print(a)
    #print(len(allnums))

    #allnums = [ [i,j,k,l] for i in range(10) for j in range(10) for k in range(10) for l in range(10)]

    for a in allnums:
        #print(a)
        final = genAll(a)    
        calculate(final,10)

    #nums = [9,8,7,6]

    #final = genAll(nums)    
    #calculate(final,10)

if __name__ == "__main__":
    main()
    