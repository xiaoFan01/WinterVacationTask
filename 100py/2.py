I = int(input())
if I<=100000:
    P = I/10
elif I<=200000:
    P = 10000 + (I-100000)*0.075
elif I <=400000:
    P = 10000 + 7500 + (I-200000)*0.05
elif I <=600000:
    P = 10000 + 7500 + 10000 + (I-400000)*0.03
elif I <=1000000:
    P = 10000 + 7500 + 10000 + 12000 + (I-600000)*0.015
else:
    P = 10000 + 7500 + 10000 + 12000 + 9000 + (I-1000000)*0.01
print(P)