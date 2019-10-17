import numpy as np
import subprocess
from tkinter import messagebox
#checking order
def check_order(N):
    if N%2==1:
       odd_magic_square=odd_even_square(0,N)
       output_file(odd_magic_square)
    if N%4==0:
       doubly_magic_square(N)
    if N%4!=0 and N%2==0:
       singley_magic_square(N)

#doubly even magic square function
def doubly_magic_square(N):
    magic_square = np.zeros((N,N), dtype=int)
    magic_flage=np.zeros((N,N), dtype=int)
    i=j=0;k1=1;k2=N**2;sm_order=int(N/4)
    for i in range(0,N):
        for j in range(0, N):
            magic_square[i,j]=k1;k1+=1;
            if i<sm_order or i>N-sm_order-1:
                if j>sm_order-1 and j<N-sm_order:
                   magic_square[i,j]=k2  
            if i>sm_order-1 and i<N-sm_order:
                if j<sm_order or j>=N-sm_order:
                   magic_square[i,j]=k2
            k2=k2-1 
    output_file(magic_square)

#odd even magic square function
def odd_even_square(start_number,order):
    magic_square = np.zeros((order,order), dtype=int)
    n = 1
    i, j = 0, order//2
    while n <= order**2:
          magic_square[i, j] = n+start_number
          n += 1
          newi, newj = (i-1) % order, (j+1)% order
          if magic_square[newi, newj]:
             i += 1
          else:
             i, j = newi, newj
    return magic_square

#singley even magic squre function
def singley_magic_square(N):
  #calculating the order of sub matrix 
    sm_order=int(N/2)
  #structuring sub magic_square matrix
    MA=odd_even_square(0,sm_order)
    s_n=sm_order**2
    MB=odd_even_square(s_n,sm_order)
    s_n=2*sm_order**2
    MC=odd_even_square(s_n,sm_order)
    s_n=3*sm_order**2
    MD=odd_even_square(s_n,sm_order)
    ex_n=int(sm_order/2)-1
    for j in range(sm_order-ex_n,sm_order):
      for i in range(0,sm_order):
        temp=MC[i,j];MC[i,j]=MB[i,j];MB[i,j]=temp
    for j in range(0,ex_n+1):
      for i in range(0,sm_order):
        if i==ex_n+1 and j==0: 
          continue
        temp=MA[i,j];MA[i,j]=MD[i,j];MD[i,j]=temp
    temp=MA[ex_n+1,ex_n+1];MA[ex_n+1,ex_n+1]=MD[ex_n+1,ex_n+1];MD[ex_n+1,ex_n+1]=temp 
    singley_magic_square=np.zeros((N,N),dtype=int)
 
 #construct total magic_square matrix.    
    for i in range(0,N):
      for j in range(0,N):
        if i<sm_order and j<sm_order:
          singley_magic_square[i,j]=MA[i,j]
        if i>=sm_order and j<sm_order:
          no1=i-sm_order
          singley_magic_square[i,j]=MD[no1,j]
        if i<sm_order and j>=sm_order:
          no2=j-sm_order
          singley_magic_square[i,j]=MC[i,no2]
        if i>=sm_order and j>=sm_order:
          no1=i-sm_order;no2=j-sm_order
          singley_magic_square[i,j]=MB[no1,no2]
    output_file(singley_magic_square)

#output functon    
def output_file(result):
  filename=str(N)+'×'+str(N)+".txt"
  np.savetxt(filename,result, fmt="%5d")
  subprocess.Popen(["notepad",filename])
  check_result(result)

def check_result(result):
   s1=0;magic_number=N*(N**2+1)/2
   for i in range(0,N):
      s1=0
      for j in range(0,N):
          s1+=result[i,j] 
      if s1!=magic_number:
        messagebox.showinfo("Waring","This is no magic square!")
        return 0
   filename="Valid_output"+str(N)+'×'+str(N)+".txt"
   np.savetxt(filename,result, fmt="%5g") 
#starting program
def main():
    print("Enter order:")
    inp=subprocess.Popen(["notepad","input.txt"])
    global N
    while inp.wait():
          pp+=1
    f=open("input.txt","r")
    content=(f.read())

#check validation of input.
    try:
      N=int(content)
    except Exception as e:
      messagebox.showinfo("Waring!","You have to input integer!, please retry")
      return 0  
    if (float(content)-int(float(content)))!=0:
       messagebox.showinfo("Waring!","You have to input integer!, please retry")
       return 0  
    N=int(content)
    if N<2:
       messagebox.showinfo("Waring!","input error!, please retry")    
       return 0
#select method             
    check_order(N)
if __name__== "__main__":
    main()




   
