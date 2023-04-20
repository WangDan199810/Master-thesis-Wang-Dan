######### Function #########
hang_lie <- function(A,hang,lie) {
  for ( i in 1:length(hang)) {
    a = A[i,]
    A[i,] = A[hang[i],]
    A[hang[i],] = a
  }
  for (j in 1:length(lie)) {
    b = A[,j]
    A[,j] = A[,lie[j]]
    A[,lie[j]] = b
  }
  return(A)
}


New_x_ij <- function(M,X_new) {
  P = 0
  for ( i in 1:length(X_new)) {
    P = rbind(P,M[i,]*X_new)
  }
  P = P[-1,]
  return(P)
}


Sumk_ij<- function(M,hang,lie) {
  H = 0  
  for (j in lie){
    H = data.frame(H,sum(M[hang,j]))
  }
  H = H[,-1]
  return(H)
}



########## Calculation########
library(readr)
table2020 <- read_csv("C:/Users/WangDan/Desktop/Input-Output_2020/Table 2020_38.csv",col_names = F)
data = as.data.frame(lapply(table2020[1:45,1:51],as.numeric))#All numeric parts, no characters.
hang = c(12,15,16,17,18,19,26,28,29,30,31,32)
lie = c(12,15,16,17,18,19,26,28,29,30,31,32)
data1 = hang_lie(data,hang,lie) #exchange the row which we want.

Q = data1[1:38,1:38]
Yy = data1[1:38,c(51,39)]
Y_i = data.frame(Yy[,1]-Yy[,2]) #Total output - total intermediate consumption. 

zj = data[39,1:38] #Total intermediate. 
ld = data[40,1:38] #salary compensation.
sc = data[41,1:38] #net production tax.
gd = data[42,1:38] #Depreciation of fixed assets.
yy = data[43,1:38] #operating profit.

# matrix block
Q11 = Q[1:length(hang),1:length(lie)]
Q12 = Q[1:length(hang),(length(lie)+1):length(Q[1,])]
Q21 = Q[(length(hang)+1):length(Q[,1]),1:length(lie)]
Q22 = Q[(length(hang)+1):length(Q[,1]),(length(lie)+1):length(Q[1,])]

X_i = data1[1:38,39]+Y_i#data1[1:42,56] #Total output.
a_ij = Q/t(X_i)
Y1 = data.frame(Y_i[1:length(hang),])
Y2 = data.frame(Y_i[(length(hang)+1):length(Q[,1]),])

a11 = a_ij[1:length(hang),1:length(lie)]
a12 = a_ij[1:length(hang),(length(lie)+1):length(Q[1,])]
a21 = a_ij[(length(hang)+1):length(Q[,1]),1:length(lie)]
a22 = a_ij[(length(hang)+1):length(Q[,1]),(length(lie)+1):length(Q[1,])]

m_a11 = matrix(unlist(a11),nrow=length(a11[,1]),ncol=length(a11[1,]))
# Matrix(unlist(a22), n row=number of rows, n col=number of columns) Convert the list into a matrix.
m_a12 = matrix(unlist(a12),nrow=length(a12[,1]),ncol=length(a12[1,]))
m_a21 = matrix(unlist(a21),nrow=length(a21[,1]),ncol=length(a21[1,]))
m_a22 = matrix(unlist(a22),nrow=length(a22[,1]),ncol=length(a22[1,]))
m_Y1 = matrix(unlist(Y1),nrow=length(Y1[,1]),ncol=length(Y1[1,]))
m_Y2 = matrix(unlist(Y2),nrow=length(Y2[,1]),ncol=length(Y2[1,]))
C1 = solve(diag(length(a22))-m_a22)  
#diag(n) generates the identity matrix, solve(A) calculates the inverse matrix of the A matrix.
# Matrix(unlist(x22), n row=38)#Convert the list into a matrix.
C2 = m_a12%*%C1 
#Cross product %*%, *dot product.
C3 = C2%*%m_a21
Rv = m_a11 + m_a12%*%C1%*%m_a21    # m_x11 + C3
Yv = m_Y1 + C2%*%m_Y2

library(carData)# Import the package where the dataset is located.
write.csv(Rv, "C:/Users/WangDan/Desktop/Input-Output_2020/Technical coefficient_2020.csv")
New_intermediate_input = data1[1:12,1:12]
#write.csv(New_intermediate_input, "C:/Users/WangDan/Desktop/Input-Output_2020/New_intermediate_input_2020.csv")



#The degree of servitization of advanced manufacturing.
AMSD_j = Sumk_ij(New_intermediate_input,1:6,7:12)/sum(Sumk_ij(New_intermediate_input,1:12,1:6))
write.csv(AMSD_j, "C:/Users/WangDan/Desktop/Input-Output_2020/AMSD_j.csv")
#W_j = Sumk_ij(New_intermediate_input,1:12,1:6)/sum(New_intermediate_input)
#AMSD = sum(AMSD_j*W_j )
sum(Sumk_ij(New_intermediate_input,1:6,7:12))
AMSD = sum(AMSD_j)
# The degree of manufacturing in modern service industry.
ASMD_j = Sumk_ij(New_intermediate_input,7:12,1:6)/sum(Sumk_ij(New_intermediate_input,1:12,7:12))
write.csv(ASMD_j , "C:/Users/WangDan/Desktop/Input-Output_2020/ASMD_j .csv")

sum(Sumk_ij(New_intermediate_input,7:12,1:6))
ASMD = sum(ASMD_j)
#综合融合度
AMSD/ASMD
#莱昂提夫逆矩阵
L = solve(diag(12)-Rv) 
#Comprehensive integration degree
CID =AMSD/ASMD
####### The degree of integration and interaction ######
L = solve(diag(12)-Rv) 
Influence_coefficient_M = Sumk_ij(L,1:6,7:12)/(sum(L[1:6,7:12])/6)
write.csv(Influence_coefficient_M , "C:/Users/WangDan/Desktop/Input-Output_2020/Influence_coefficient_M_2020 .csv")
Influence_coefficient_A = Sumk_ij(L,7:12,1:6)/(sum(L[7:12,1:6])/6)
write.csv(Influence_coefficient_A , "C:/Users/WangDan/Desktop/Input-Output_2020/Influence_coefficient_A_2020 .csv")

