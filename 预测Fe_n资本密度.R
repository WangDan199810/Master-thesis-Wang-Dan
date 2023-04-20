library(zoo)
library(tseries)
library(forecast)
library(TTR)

Data = read.csv("C:/Users/WangDan/Desktop/The united states/Tendancy/Fe_n.csv",header=T,sep=",")
# 第一行作为行名##########  
#row.names(Data) <- Data$sector
#Data = Data[,-1]
Data
###########

y1 = unlist(Data[1,])



# 时间序列部分 #############################################
y1_ts = ts(y1) # 将y作为时间序列 


# y_1
auto.arima(y1_ts) # 自动分析时间序列的ARIMA(p,d,q)，p=?，q=?，d=?
pre_y1 = arima(y1_ts,order=c(1,1,0)) # 在ARIMA(p,d,q)下预测，得到系数与AIC
wine_y1 <- forecast(pre_y1,h=6,level=c(99.5)) # 未来1个周期的值，设置上下95%的置信区间
wine_y1



# 线性回归部分 #############################################
x = c(0.0338,0.0283,0.0159,0.0227,0.0268,0.0339,0.0323,0.0285,0.0384,-0.0036,0.0164,0.0316,0.0207,0.0146,0.0162,0.0012,0.0126,0.0213)
# 需要预测哪几年的Fe？
new <- data.frame(x = c(0.0244,0.0181,0.0123,0.0470,0.08,0.028,0.03))  

# 部门1
summary(lm(y1~x))
Fe_n = predict(lm(y1~x), new)
Fe_n



# 对比分析 ###################

# 时间序列
# c(y1,wine_y1$mean)将原本的y1数据，末尾加上预测值wine_y1$mean
var( c(y1,wine_y1$mean) ) # 0.6411496

# 线性回归
var( c(y1,Fe_n) ) # 0.6678581



# 对于部门1，使用时间序列得到的方差更小，推荐：时间序列
# 对于部门2，使用时间序列得到的方差更小，推荐：时间序列
# 对于部门3，使用时间序列得到的方差更小，推荐：时间序列

