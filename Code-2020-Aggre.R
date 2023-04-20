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
table2020 <- read_csv("C:/Users/WangDan/Desktop/Input-Output_2020/2020.csv",col_names = F)
data2020 = as.data.frame(lapply(table2020[7:166,4:169],as.numeric))
HL = list( 1:5,6:11,12:26,27:32,33:34,35:36,37:40,41:42,43:49,50:51,52:53,54:60,61:65,66,67:78,79:83,84:89,90:95,96,97:99,100,101,102,103:108,109:110,111:122,123:124,125:129,130:132,133,134:135,136:138,139:141,142:143,144,145:146,147:151,152:153,154,155,156,157,158,159,160,161,162,163,164,165,166)
data2020_3 = merge(data2020,HL)
library(carData) # Import the package where the dataset is located.
write.csv(data2020_3, "38_industries—2020.csv")
