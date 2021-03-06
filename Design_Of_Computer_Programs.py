from collections import defaultdict
import random

def test_shuffler(shuffler, deck = 'abcd', n=100000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1./factorial(len(deck))
    ok = all((0.7 <= counts[item]/e <= 1.3)
             for item in counts)
    name = shuffler.__name__
    print '%s(%s)%s' % (name, deck, ('ok' if ok else '*** BAD ***'))
    print '   ',
    for item, count in sorted(counts.items()):
        print '%s:%4.1f' % (item, count*100./n),
        print

def factorial(n): return 1 if (n<=1) else n*factorial(n-1)

def shuffle3(deck):
    N=len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))

def swap(deck, i, j):
    deck[i], deck[j] = deck[j], deck[i]

test_shuffler(shuffle3)

print 100000/factorial(4)
