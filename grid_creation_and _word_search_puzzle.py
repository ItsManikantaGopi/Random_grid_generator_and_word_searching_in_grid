#random grid creation
def crt_grid(n):
	vl=list(map(chr,range(65,91)))+list(map(chr,range(97,123)))+list(map(str,range(0,10)))
	d=dict(enumerate(vl,1))
	l=[]
	from random import randint as rand
	for i in range(n):
		m=[]
		for j in range(n):
			m.append(d[rand(1,62)])
		l.append(m)
	return l
#printing grid function by passing random grid created
def print_grid(l):
	for j in range(len(l)):
		for i in range(len(l[j])):
			print(l[j][i],end=" ")
		print()
#printing grid function by passing random grid created along with index values
def print_grid_ind(l):
	for j in range(len(l)):
		for i in range(len(l[j])):
			print((j,i),l[j][i],end=" ")
		print()
#searching the word after finding the first letter in the grid
def srch(l,b,j,k):
	m=[[1,1],[-1,-1],[1,-1],[-1,1],[1,0],[0,1],[-1,0],[0,-1]]
	n=len(l)
	t,u=j,k
	for i in m:
		a=b[0]
		x=i[0]
		y=i[1]
		for p in range(len(b)-1):
			if((j+x)<n or (k+y)<n):
				if((j+x)<n):
					j+=x
				if((k+y)<n):
					k+=y
				a+=l[j][k]
			else:
				continue
		j,k=t,u
		if(a==b):
			break
	if(a==b):
		return True
	else:
		return False
#function to find index of the first letter and to search it in grid by passing the col and row
def word_find(l,n,b):
        flag=0
        for i in range(n):
                for j in range(n):
                        if(b[0]==l[i][j]):
                                if(srch(l,b,i,j)):
                                        print("True")
                                        print("found at row {} and column {}".format(i+1,j+1))
                                        flag=1
                                else:
                                        continue
        if(flag==0):
                print("word not found")


n=int(input("enter grid dimensions:="))
l=crt_grid(n)
print_grid(l)
#print_grid_ind(l)
while 1:
        b=input("enter word to search:=")
        word_find(l,n,b)
        t=input("enter -1 to exit:=")
        if(t=="-1"):
                print("bye bye")
                break

