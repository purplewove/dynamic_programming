'''
Created on Nov 10, 2015

@author: templetonc
'''

class Binomials():
    def __init__(self, n):
        self.n = n
        self.coeffs = []
        
    def __iter__(self):
        for i in range(self.n):
            self.coeffs.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    self.coeffs[i].append(1)
                else:
                    self.coeffs[i].append(self.coeffs[i-1][j-1] + self.coeffs[i-1][j])
            yield self.coeffs[i]

if __name__ == '__main__':
    bs = Binomials(10)
    for b in bs:
        print b