#! /bin/python3

from unicodedata import digit
from gmpy2 import *
from scipy.special import comb
import numpy as np
from decimal import Decimal  
from bigfloat import BigFloat, precision

def probability_of_double_spend_attack(q,z,n):
	p=round(1-q,3) 
	first_part=0
	second_part=0
	for k in range(z,2*n-z): 
		first_part+=comb(z+k-1,k)*pow(p,z)*pow(q,k)
	for k in range(0,z): 
		sum_internal=pow(q,z-k) 
		difference=[pow(q,z-k)]
		for i in range(1,n-z+1,1): 
			temp=0
			for j in range(0,i):
				temp+=difference[j]*comb(2*i-2*j,i-j)*pow(p*q,i-j)
			difference.append(comb(z-k+2*i,i)*pow(p,i)*pow(q,z-k+i)-temp)
			sum_internal+=difference[i]
		second_part+= comb(z+k-1,k)*pow(p,z)*pow(q,k)*(sum_internal)
	return first_part+second_part
def main():
    for i in range(50,550,50):
        print('n=',i)
        for k in np.arange(0.1, 0.5, 0.05):
            j=0
            print(' q: ',round(k,3),':',end='')
            while(True):
                j=j+5
                var=probability_of_double_spend_attack(round(k,3),j,i)
                print(var,end=':') 
                if(j==i):
                    print(end='\n') 
                    break

if __name__ == "__main__":
    main()
