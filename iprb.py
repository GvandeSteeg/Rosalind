"""
http://rosalind.info/problems/iprb/
k = homozygous dominant
m = heterozygous
n = homozygous recessive

given k + m + n, return the probability that two randomly selected mating organisms will produce an individual
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k + k = 1
    A   A
A   AA  AA
A   AA  AA

k + m = 1
    A   a
A   AA  Aa
A   AA  Aa

k + n = 1
    a   a
A   Aa  Aa
A   Aa  Aa

m + m = 0.75
    A   a
A   AA  Aa
a   Aa  aa

m + n = 0.5
    a   a
A   Aa  Aa
a   aa  aa

n + n = 0
    a   a
a   aa  aa
a   aa  aa
"""

k = 2
m = 2
n = 2

print((1 + 1 + 1 + .75 + .5 + 0) / (k + m + n)) # should be 0.78333
