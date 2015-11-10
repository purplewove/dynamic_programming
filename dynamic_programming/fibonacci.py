'''
Created on Nov 10, 2015

@author: templetonc
'''

class Fibonaccis():
    def __init__(self, n):
        self.n = n
        self.f = []
        self.f.append(0)
        self.f.append(1)
        
    def __iter__(self):
        yield self.f[0]
        yield self.f[1]
        for i in range(2, self.n):
            self.f.append(self.f[i - 1] + self.f[i - 2])
            yield self.f[i]
            
            
if __name__ == '__main__':
    fi = Fibonaccis(100)
    for num in fi:
        print num