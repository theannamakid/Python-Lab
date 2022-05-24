def Matrix_Read(m,n):                                                   #
    A=[]                                                                #
    print()                                                             #
    for i in range (m):                                                 #
        a=[]                                                            # FUNCTION TO READ THE MATRIX
        for j in range (n):                                             #
            a.append(int(input("Enter the value of matrix : ")))        #
        A.append(a)                                                     #
    print()                                                             #
    return A                                                            #

def Matrix_Print(A,m,n):                #
    for i in range (m):                 #
        for j in range (n):             # FUNCTION TO PRINT THE MATRIX
            print(A[i][j],end = " ")    #
        print()                         #

def Matrix_Add(A,B,m,n):                   #
    S=[]                                   #
    for i in range(m):                     #
        s=[]                               #
        for j in range(n):                 # FUNCTION TO ADD THE MATRICES
            sum=A[i][j]+B[i][j]            #
            s.append(sum)                  #
        S.append(s)                        #
    return S                               #
    
m=int(input("Enter row of matrix A : "))                #
n=int(input("Enter column of matrix A : "))             #
A=Matrix_Read(m,n)                                      # READ THE MATRIX
x=int(input("Enter row of matrix B : "))                #
y=int(input("Enter column of matrix B : "))             #
B=Matrix_Read(x,y)                                      #

print("\nMatrix A :")               #
Matrix_Print(A,m,n)                 # DISPLAY THE MATRIX
print("\nMatrix B :")               #
Matrix_Print(B,x,y)                 #

if(m==x and n==y):                              #
    S=Matrix_Add(A,B,m,n)                       #
    print("\nSum of Matrices : ")               # CONDITION FOR ADDING MATRICES
    Matrix_Print(S,m,n)                         #
else:                                           #
    print("Row or Column does not match")       #
