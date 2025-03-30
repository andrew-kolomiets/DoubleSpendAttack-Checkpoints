#! /bin/python3

import sympy as sp
from gmpy2 import *
from decimal import Decimal
from bigfloat import BigFloat, precision

def probability_of_double_spend_attack(q,z,n):
    p=round(1-q,3);second_part=0
    first_part = sum(
        sp.binomial(z+k-1,k)*pow(p,z)*pow(q,k) for k in range(z,2*n-z+1)
    )
    for k in range(0, z):
        sum_internal, difference = [pow(q,z-k)], [pow(q, z-k)]
        i=1
        while i<=2*n-z:
            temp=0
            j=0
            while j<i:
                temp+=round(difference[j]*sp.binomial(2*i-2*j,i-j)*pow(p*q,i-j),100)
                j += 1
            difference.append(sp.binomial(z-k+2*i,i)*pow(p,i)*pow(q,z-k+i)-temp)
            sum_internal=sum(difference)
            i+=1
        second_part+=sp.binomial(z+k-1,k)*pow(p,z)*pow(q,k)*sum_internal
    return first_part + second_part
    

def main():
    for i in range(50,200,50):
        print('n=',i)
        for k in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45]:
            j=0
            print('q: ',round(k,3),':',end='')
            while(True):
                j=j+1
                temp=probability_of_double_spend_attack(round(k,3),j,i)
                if(temp<0.001 and j<i):
                    print(j,':',temp,end='\n')
                    break
                if(j==i or j>i):
                    print(i, ':',
                          probability_of_double_spend_attack(round(k,3),i,i),
                          end='\n')
                    break
                    
if __name__=="__main__":
    main()


