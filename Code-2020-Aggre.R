library(readr)
######### Function #########
merge<- function(P,HL) {
  M = 0
  for ( S in HL) { # Column to merge
    L = 0
    for (j in S){
      a = P[,j]
      L = a+L
    }
    M = data.frame(M,L)
  }
  M = M[,-1]
  K = 0
  for ( S in HL) { # Row to merge
    H = 0
    for (i in S){
      a = M[i,]
      H = a+H
    }
    K = rbind(K,H)
  }
  K = K[-1,]
  return(K)
}

######### calculation ########
table2020 <- read_csv("C:/Users/WangDan/Desktop/IOTs China/2020/2020 .csv",col_names = F)
data2020 = as.data.frame(lapply(table2020[7:166,4:169],as.numeric))
HL = list(c(54:60,67:96),c(111:122,125:138),c(1:53,61:66,97:110,123:124,139:153),154,155,156,157,158,159,160,161,162,163,164,165,166)
data2020_3_sectors = merge(data2020,HL)
library(carData) # Import the package where the dataset is located.
write.csv(data2020_3_sectors, "C:/Users/WangDan/Desktop/IOTs China/2020/3_sectors.csv")
