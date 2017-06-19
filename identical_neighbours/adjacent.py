import heapq
from collections import Counter

def reorder(str):
    counts = Counter(str)
    h = []
    reordered = ''

    for ch, count in counts.iteritems():
        heapq.heappush(h, (-1*count, ch))

    last_tuple = None    

    while h:
        count, ch = heapq.heappop(h)
        reordered += ch
    
        if last_tuple:
            heapq.heappush(h, last_tuple)
    
        count += 1
        last_tuple = (count, ch) if count != 0 else None

    return reordered

if __name__ == '__main__':
    print reorder('hellothere')
