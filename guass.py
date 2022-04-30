


def doi_dong(A,B):
	l=len(A)
	for i in range (l):
		A[i],B[i]=B[i],A[i]


def chuyenhesove1(A,j):
	l=len(A)
	chia=A[j]
	if(chia!=0):
		for i in range(l): 
			A[i]=A[i]/chia

def congvoimatrankhac(A,B,n):
	l=len(A)
	for i in range (l):
		B[i]+=A[i]*n
def Gauss_elimination(A):
	m=len(A)
	n=len(A[0])

	for i in range(m):
		dieukien=0
		for j in range(i,m):
			if(A[j][i]!=0):
				dieukien=1
				doi_dong(A[i],A[j])
				break
		if(dieukien==0):
			continue
		chuyenhesove1(A[i],i)
		for j in range(i+1,m):
			bientam=-(A[j][i]/A[i][i])
			congvoimatrankhac(A[i],A[j],bientam)
	print("Ma tran bac thang: ")
	for i in range(len(A)):
		print(A[i])
def back_substitution(A):
	m=len(A)
	n=len(A[0])
	for i in range(m):
		if A[i][i]==0:
			if(A[i][n-1]!=0):
				print("VN")
				return
			elif ((m-n+1) <=0):
				print("VSN")
				return
	x=[0]
	for i in range (n-2,-1,-1): #Chay tu n-1 den 0 (so phan tu nghiem)
		k=0
		b=A[i][n-1]
		for j in range(i+1,n-1):
			b-=(A[i][j]*x[k])

			k=k+1
		x.insert(0,b)
	x.pop()
	print("Nghiem:")
	for i in range(len(x)):
		print("x",i,"=",x[i])




A=[[1,-2,3,-3],[2,2,0,0],[0,-3,4,1],[1,0,1,-1]]
Gauss_elimination(A)
back_substitution(A)
