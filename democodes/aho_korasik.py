#!/usr/bin/env python
#http://ru.stackoverflow.com/questions/383679/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D1%8F%D1%8E%D1%89%D0%B8%D1%85%D1%81%D1%8F-%D1%81%D1%82%D1%80%D0%BE%D0%BA
#Ахо-Корасик-подобный алгоритм
import re
import sys
from collections import Counter

def main():
    # load substrings from file2
    with open('file2', 'rb') as file2:
        substrings = {line.strip() for line in file2} # unique lines
        substrings = filter(None, substrings) # filter blank lines
        substrings = sorted(substrings, key=len, reverse=True) # longest first
        pattern = b"|".join(map(re.escape, substrings))
        find_substrings = re.compile(pattern).findall

    # count substrings in file1
    counter = Counter()
    counter_update = counter.update # cache the lookup (for CPython)
    with open('file1', 'rb') as file1:
        for line in file1:
            counter_update(find_substrings(line))

    # write substrings frequencies
    write = getattr(sys.stdout, 'buffer', sys.stdout).write
    for substring, count in counter.most_common(): # most common first
        write(substring)
        write(b' ')
        write(str(count).encode())
        write(b'\n')

main()
