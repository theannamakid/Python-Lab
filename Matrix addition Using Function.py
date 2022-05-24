def Matrix_Read(A,m,n):                                                 #
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
    
A=[]                                                    #
m=int(input("Enter row of matrix A : "))                #
n=int(input("Enter column of matrix A : "))             #
A=Matrix_Read(A,m,n)                                    # TO READ THE MATRIX
B=[]                                                    #
x=int(input("Enter row of matrix B : "))                #
y=int(input("Enter column of matrix B : "))             #
B=Matrix_Read(B,x,y)                                    #

print("\nMatrix A :")               #
Matrix_Print(A,m,n)                 # TO DISPLAY THE MATRIX
print("\nMatrix B :")               #
Matrix_Print(B,x,y)                 #

if(m==x and n==y):                              #
    S=Matrix_Add(A,B,m,n)                       #
    print("\nSum of Matrices : ")               # CONDITION FOR ADDING MATRICES
    Matrix_Print(S,m,n)                         #
else:                                           #
    print("Row or Column does not match")       #
