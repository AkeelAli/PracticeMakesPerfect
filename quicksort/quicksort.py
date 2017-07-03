from random import randint 

def partition(pivot_i, A, low, high):
    '''
    [   <   |   ==  |   ??  |   >   ]
             ^       ^     ^
            lt      eq     gt
    less than, equal, unclassified, greater than
    '''
    lt, eq, gt = low, low, high
    pivot = A[pivot_i]

    while (eq <= gt):  #NOTE: <=
        if A[eq] > pivot:
            A[eq], A[gt] = A[gt], A[eq]
            gt = gt - 1
        elif A[eq] < pivot:
            A[eq], A[lt] = A[lt], A[eq]
            lt, eq = lt + 1, eq + 1
        else:
            eq += 1

    return lt

def quicksort(l):

    def quicksort_helper(l, low, high):
        if low >= high:
            return

        pivot_i = randint(low, high)
        #print 'pivot %d, low %d, high %d' % (l[pivot_i], low, high)
        pivot_i = partition(pivot_i, l, low, high) # NOTE: pick up new pivot_i to parition around
        #print l

        quicksort_helper(l, low, pivot_i - 1)
        quicksort_helper(l, pivot_i + 1, high)
    
    
    quicksort_helper(l, 0, len(l) - 1)    
    return l


if __name__ == '__main__':
#    l = [6, 213, 6, 324, 1235, 92, 45]
#    for _ in range(10):
#        pivot_i = randint(0,len(l)-1)
#        print 'partition of %s using pivot %d is' % (l,l[pivot_i])
#        partition(pivot_i,l)
#        print l
#        print

    print quicksort([randint(-10,10) for x in range(10)])
