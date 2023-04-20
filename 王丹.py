import pandas as pd
import numpy as np

# b.sum()，np.sum(b) 这两个都能将数组b的所有元素求和。c.sum(),np.sum(c)这两个都能将矩阵c的所有元素求和
# 对于二维数组b： b.sum(axis=0)指定对数组b对每列求和，b.sum(axis=1)是对每行求和
# 对于矩阵c： c.sum(axis=0)指定对矩阵c对每列求和，c.sum(axis=1)是对每行求和



def wang(data):
    matrix = np.mat(data)
    Q = matrix[0:3,0:3]
    Yy = matrix[0:3,3:12] 
    Y_i = Yy[:,0]+Yy[:,1]+Yy[:,2]+Yy[:,3]+Yy[:,4]+Yy[:,5]+Yy[:,6]+Yy[:,7]+Yy[:,8]
    TXS_IMP_FIN_j = matrix[3,0:3]
    TXS_IMP_FIN_n = matrix[3,3:12]
    TXS_INT_FIN_j = matrix[4,0:3] 
    TXS_INT_FIN_n = matrix[4,3:12]
    GFCF_i = matrix[0:3,6]
    INVNT_i = matrix[0:3,7]
    X_i = matrix[7,0:3]
    VALU_j = matrix[6,0:3]
    W_j = matrix[8,0:3] 
    ONT_j = matrix[9,0:3] 
    Profit = matrix[10,0:3] 
    GDP = np.sum(VALU_j) + np.sum(TXS_INT_FIN_j) + np.sum(TXS_INT_FIN_n)
    # np.append(a,b)所有元素合并为行向量，np.append(a,b,axis=0) 行合并，由2*2变为4*2，np.append(a,b,axis=1) 列合并，由2*2变为2*4
    a_ij = np.append(np.append(Q[:,0]/X_i[0,0],Q[:,1]/X_i[0,1],axis=1),Q[:,2]/X_i[0,2],axis=1)
    aq_j = (X_i-VALU_j-TXS_INT_FIN_j)/X_i
    aq = (np.sum(X_i) - np.sum(VALU_j) - np.sum(TXS_INT_FIN_j))/np.sum(X_i)
    tq_j = TXS_INT_FIN_j/X_i
    qw_j =  W_j/VALU_j
    qt_j = ONT_j/VALU_j
    Prh_j = np.mat(np.array(1-aq_j-tq_j)*np.array(1-qw_j-qt_j)*np.array(X_i))
    Y_qi = Y_i/GDP
    tq_n1 = np.sum(TXS_INT_FIN_n)/GDP
    CP_i = GFCF_i+INVNT_i
    CP = np.sum(CP_i)
    rn_j = np.array(CP_i) / np.array(Prh_j.T)
    rn_n1 = CP/GDP
    #        0   1  2   3    4    5   6    7    8     9   10   11   12   13  14
    return CP_i,X_i,CP,GDP,rn_n1,aq,aq_j,tq_j,tq_n1,qw_j,qt_j,Y_qi,rn_j,a_ij,X_i


def dan(Data_1,Data_2):
    Fe_i =  np.array(wang(Data_1)[0]) / np.array(wang(Data_2)[1].T-wang(Data_1)[1].T )   # CP_i/(X_2-X_1)
    Fe_n =  wang(Data_1)[2] / (wang(Data_2)[3]-wang(Data_1)[3] )   # CP/(GDP_2001-GDP)
    X_new_n = (wang(Data_1)[4]*((1-wang(Data_1)[5])*np.sum(wang(Data_1)[1])+wang(Data_1)[8]*wang(Data_1)[3]))/Fe_n
    X_new = (np.array(wang(Data_1)[12].T)*np.array(1-wang(Data_1)[6]-wang(Data_1)[7])*np.array(1-wang(Data_1)[9]-wang(Data_1)[10])*np.array(wang(Data_1)[5]*wang(Data_1)[1] + wang(Data_1)[11].T*wang(Data_1)[3]))/Fe_i.T
    return Fe_i,Fe_n,X_new_n,X_new



Data2000 = pd.read_csv("USA/2000.csv",header=None).values
Data2001 = pd.read_csv("USA/2001.csv",header=None).values
Data2002 = pd.read_csv("USA/2002.csv",header=None).values
Data2003 = pd.read_csv("USA/2003.csv",header=None).values
Data2004 = pd.read_csv("USA/2004.csv",header=None).values
Data2005 = pd.read_csv("USA/2005.csv",header=None).values
Data2006 = pd.read_csv("USA/2006.csv",header=None).values
Data2007 = pd.read_csv("USA/2007.csv",header=None).values
Data2008 = pd.read_csv("USA/2008.csv",header=None).values
Data2009 = pd.read_csv("USA/2009.csv",header=None).values
Data2010 = pd.read_csv("USA/2010.csv",header=None).values
Data2011 = pd.read_csv("USA/2011.csv",header=None).values
Data2012 = pd.read_csv("USA/2012.csv",header=None).values
Data2013 = pd.read_csv("USA/2013.csv",header=None).values
Data2014 = pd.read_csv("USA/2014.csv",header=None).values
Data2015 = pd.read_csv("USA/2015.csv",header=None).values
Data2016 = pd.read_csv("USA/2016.csv",header=None).values
Data2017 = pd.read_csv("USA/2017.csv",header=None).values
Data2018 = pd.read_csv("USA/2018.csv",header=None).values





Fe_i_00_01,Fe_n_00_01,X_new_n_00_01,X_new_00_01 = dan(Data2000,Data2001)
Fe_i_01_02,Fe_n_01_02,X_new_n_01_02,X_new_01_02 = dan(Data2001,Data2002)
Fe_i_02_03,Fe_n_02_03,X_new_n_02_03,X_new_02_03 = dan(Data2002,Data2003)
Fe_i_03_04,Fe_n_03_04,X_new_n_03_04,X_new_03_04 = dan(Data2003,Data2004)
Fe_i_04_05,Fe_n_04_05,X_new_n_04_05,X_new_04_05 = dan(Data2004,Data2005)
Fe_i_05_06,Fe_n_05_06,X_new_n_05_06,X_new_05_06 = dan(Data2005,Data2006)
Fe_i_06_07,Fe_n_06_07,X_new_n_06_07,X_new_06_07 = dan(Data2006,Data2007)
Fe_i_07_08,Fe_n_07_08,X_new_n_07_08,X_new_07_08 = dan(Data2007,Data2008)
Fe_i_08_09,Fe_n_08_09,X_new_n_08_09,X_new_08_09 = dan(Data2008,Data2009)
Fe_i_09_10,Fe_n_09_10,X_new_n_09_10,X_new_09_10 = dan(Data2009,Data2010)
Fe_i_10_11,Fe_n_10_11,X_new_n_10_11,X_new_10_11 = dan(Data2010,Data2011)
Fe_i_11_12,Fe_n_11_12,X_new_n_11_12,X_new_11_12 = dan(Data2011,Data2012)
Fe_i_12_13,Fe_n_12_13,X_new_n_12_13,X_new_12_13 = dan(Data2012,Data2013)
Fe_i_13_14,Fe_n_13_14,X_new_n_13_14,X_new_13_14 = dan(Data2013,Data2014)
Fe_i_14_15,Fe_n_14_15,X_new_n_14_15,X_new_14_15 = dan(Data2014,Data2015)
Fe_i_15_16,Fe_n_15_16,X_new_n_15_16,X_new_15_16 = dan(Data2015,Data2016)
Fe_i_16_17,Fe_n_16_17,X_new_n_16_17,X_new_16_17 = dan(Data2016,Data2017)
Fe_i_17_18,Fe_n_17_18,X_new_n_17_18,X_new_17_18 = dan(Data2017,Data2018)

Data = [Data2000,Data2001,Data2002,Data2003,Data2004,Data2005,Data2006,Data2007,Data2008,Data2009,Data2010,Data2011,Data2012,Data2013,Data2014,Data2015,Data2016,Data2017,Data2018]
year = 0
for i in range(len(Data)-1):
    Fe_i,Fe_n,X_new_n,X_new = dan(Data[i],Data[i+1])
    year = year +1
    print("\n",year,"到",year+1,"年的数据\n",Fe_i,"\n")

for i in Data:
    print("GDP\n", wang(i)[3],"\n")
  
for i in Data:
    print("X_i\n", wang(i)[14],"\n") 

    
Data_all = [Data2000,Data2001,Data2002,Data2003,Data2004,Data2005,Data2006,Data2007,Data2008,Data2009,Data2010]

# for i in Data_all:
    # print( "\n a_ij= \n",wang(i)[13],"\n" )
    


def R_ (Data):
     R1 = np.append( wang(Data)[13] , wang(Data)[11] ,axis=1)
     R2 = np.append( 1-wang(Data)[6] , np.mat(wang(Data)[8]) ,axis=1)
     R =  np.append( R1 , R2 ,axis=0)
     return R
 
def M_Δ_year(Data_1,Data_2):
    α_j = np.array(wang(Data_1)[12].T)*np.array(1-wang(Data_1)[6]-wang(Data_1)[7])*np.array(1-wang(Data_1)[9]-wang(Data_1)[10])
    Fe = dan(Data_1,Data_2)[0]
    rn_n1 = wang(Data_1)[4]
    Fe_n = dan(Data_1,Data_2)[1]
    M = np.mat( [[α_j[0,0]/Fe[0,0],0,0,0],[0,α_j[0,1]/Fe[1,0],0,0],[0,0,α_j[0,2]/Fe[2,0],0],[0,0,0,rn_n1/Fe_n]] )
    return M 

def D_Δ_year(Data_1,Data_2):
    return R_ (Data_1)*M_Δ_year(Data_1,Data_2)

print( "\n R~ \n",R_ (Data2017),"\n" )

print( "\n M= \n",M_Δ_year(Data2017,Data2018),"\n" )

print( "\n D= \n",R_ (Data2017)*M_Δ_year(Data2017,Data2018),"\n" )


D_00_01 = D_Δ_year(Data2000,Data2001)
D_01_02 = D_Δ_year(Data2001,Data2002)
D_02_03 = D_Δ_year(Data2002,Data2003)
D_03_04 = D_Δ_year(Data2003,Data2004)
D_04_05 = D_Δ_year(Data2004,Data2005)
D_05_06 = D_Δ_year(Data2005,Data2006)
D_06_07 = D_Δ_year(Data2006,Data2007)
D_07_08 = D_Δ_year(Data2007,Data2008)
D_08_09 = D_Δ_year(Data2008,Data2009)
D_09_10 = D_Δ_year(Data2009,Data2010)
D_10_11 = D_Δ_year(Data2010,Data2011)
D_11_12 = D_Δ_year(Data2011,Data2012)
D_12_13 = D_Δ_year(Data2012,Data2013)
D_13_14 = D_Δ_year(Data2013,Data2014)
D_14_15 = D_Δ_year(Data2014,Data2015)
D_15_16 = D_Δ_year(Data2015,Data2016)
D_16_17 = D_Δ_year(Data2016,Data2017)
D_17_18 = D_Δ_year(Data2017,Data2018)

print("\n D:2017-2018\n",D_17_18 ,"\n")



# Fe_i =  np.array(wang(Data2000)[0]) / np.array(wang(Data2001)[1].T-wang(Data2000)[1].T )   # CP_i/(X_2001-X_i)
# Fe_n =  wang(Data2000)[2] / (wang(Data2001)[3]-wang(Data2000)[3] )   # CP/(GDP_2001-GDP)
# X_new_n = (wang(Data2000)[4]*((1-wang(Data2000)[5])*np.sum(wang(Data2000)[1])+wang(Data2000)[8]*wang(Data2000)[3]))/Fe_n
# # X_new_n = (rn_n1*((1-aq)*sum(X_i)+tq_n1*GDP))/Fe_n

# X_new1 = (np.array(wang(Data2000)[12])*np.array((1-wang(Data2000)[6]-wang(Data2000)[7]).T)*np.array((1-wang(Data2000)[9]-wang(Data2000)[10]).T)*np.array(wang(Data2000)[5]*wang(Data2000)[1].T + wang(Data2000)[11]*wang(Data2000)[3]))/Fe_i
# X_new2 = (np.array(wang(Data2000)[12].T)*np.array(1-wang(Data2000)[6]-wang(Data2000)[7])*np.array(1-wang(Data2000)[9]-wang(Data2000)[10])*np.array(wang(Data2000)[5]*wang(Data2000)[1] + wang(Data2000)[11].T*wang(Data2000)[3]))/Fe_i.T
# # X_new = (rn_j*(1-aq_j-tq_j)*(1-qw_j-qt_j)*(aq*X_i+Y_qi*GDP))/Fe_i

# print("\n Fe_i=\n",Fe_i,"\n Fe_n=\n",Fe_n,"\n X_new_n=\n",X_new_n,"\n X_new行=\n",X_new1,"\n X_new列=\n",X_new2)

#P = [0.4474*exp(0.029t)+0.0433*exp(0.013t)+0.1191*exp(0.003t) 0.1140*exp(0.029t)-0.1529*exp(0.013t)+0.0398*exp(0.003t) 0.1429*exp(0.029t)-0.0494*exp(0.013t)-0.0934*exp(0.003t)
#     0.9542*exp(0.029t)-1.5717*exp(0.013t)+0.6175*exp(0.003t) 0.2432*exp(0.029t)+0.5548*exp(0.013t)+0.2018*exp(0.003t) 0.3048*exp(0.029t)+0.1793*exp(0.013t)-0.4842*exp(0.003t)
#     0.9684*exp(0.029t)-0.1024*exp(0.013t)-0.8659*exp(0.003t) 0.2468*exp(0.029t)+0.0361*exp(0.013t)-0.2830*exp(0.003t) 0.3093*exp(0.029t)+0.0116*exp(0.013t)+0.6789*exp(0.003t)];






