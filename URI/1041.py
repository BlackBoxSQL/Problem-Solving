# x,y=map(float, input().split())
x = float(input())
y = float(input())

if (x==y==0):
    print("Origem")
elif(x==0):
    print("Eixo X")
elif(y==0):
    print("Eixo Y")
elif(x>0)and(y>0):
    print("Q1")
elif(x<0)and(y>0):
    print("Q2")
elif(x<0) and (y<0):
    print("Q3")
elif(x>0)and(y<0):
    print("Q4")


#runtime error