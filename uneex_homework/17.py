'''
Ввести последовательность четвёрок целых чисел вида (s, d, m, n), (…), ….
Для каждой четвёрки составить целочисленную последовательность
{ai}: a0=s, ai+1=ai/d+m, если ai делится на d и ai+1=ai+n в противном случае.
Последовательность заканчивается на i-м элементе, если i+1-й будет ему равен,
в противном случае (цикл из нескольких значений или неограниченный рост)
последовательность считается бесконечной.
Если последовательность, полученная из очередной четвёрки, заканчивается,
начинается последовательность, полученная из следующей четвёрки.
Ввести k и вывести k-й член этой общей последовательности или "NO",
если в ней меньше k элементов.

Input:

(4,2,5,3),(3,5,8,1),(5,3,8,2),(3,4,2,6)
30
Output:

13
'''

t = ((4,2,5,3),(3,5,8,1),(5,3,8,2),(3,4,2,6))
k = 30




def gen_seq(s, d, m, n):
    prev, curr = None, s
    while prev != curr:
        yield curr
        prev, curr = curr, (curr + n) if curr % d else (curr // d + m)

def catseq(t):
    for t in t:
        yield from gen_seq(*t)

for i,e in enumerate(catseq(t)):
    if i == k:
        print(e)
        break
else:
    print("NO")