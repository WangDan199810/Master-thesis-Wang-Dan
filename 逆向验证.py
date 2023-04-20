#导入
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import e


def f2(t,X):
  #x1,x2...xn = X
  x,y,z = X
  #dx1dt=...,dx2dt=...,dxndt=...
  dxdt = 0.01951666*x + 0.00133843*y + 0.00318622*z + (-469592705400698.0*(-7.11084159219985e-18*2.7183**(0.009*t) + 0.115121700488119*2.7183**(0.02*t) + 0.419787210870817*2.7183**(0.031*t) - 0.0122335118786456*2.7183**(0.035*t) - 4.05423849873798e-17*2.7183**(0.042*t) + 0.286650117988355*2.7183**(0.046*t) - 0.375178142303231*2.7183**(0.057*t) - 0.0461350644461428*2.7183**(0.061*t) - 0.388012310719272*2.7183**(0.072*t) + 1.00691919688197e-16*2.7183**(0.087*t))/(8.82058876317093e-22*2.7183**(0.012*t) - 1.55946918657379e-6*2.7183**(0.023*t) - 3.11625605937949e-6*2.7183**(0.034*t) - 1.50771899240728e-6*2.7183**(0.038*t) + 9.37248327289653e-6*2.7183**(0.045*t) + 0.118790692457187*2.7183**(0.049*t) - 1.8384089113991e-22*2.7183**(0.056*t) + 0.433217928028111*2.7183**(0.06*t) - 5.68591534242605e-6*2.7183**(0.064*t) + 2.48588931504467e-6*2.7183**(0.071*t) + 0.448026803234065*2.7183**(0.075*t) + 2.5709271109231e-6*2.7183**(0.086*t) - 3.69936866623276e-16*2.7183**(0.09*t) + 3.76899956269262e-16*2.7183**(0.101*t) - 1.30192864240577e-31*2.7183**(0.116*t)) + 1.52713249102982e+15*(4.43905779647398e-22*2.7183**(0.015*t) + 6.70904334959811e-7*2.7183**(0.026*t) - 0.0350345577242675*2.7183**(0.037*t) - 1.10497361365879e-6*2.7183**(0.041*t) - 0.127764237131204*2.7183**(0.048*t) + 0.0563674083248894*2.7183**(0.052*t) - 1.10858669652723e-5*2.7183**(0.059*t) - 0.0262949241502832*2.7183**(0.063*t) + 0.00219813732796143*2.7183**(0.067*t) - 6.35936846870623e-23*2.7183**(0.07*t) - 0.363604153950973*2.7183**(0.074*t) + 0.346639601684138*2.7183**(0.078*t) - 7.17245965808893e-6*2.7183**(0.085*t) + 0.033688063066917*2.7183**(0.089*t) + 0.008305338387095*2.7183**(0.093*t) - 0.181778719216603*2.7183**(0.1*t) + 0.47528610596299*2.7183**(0.104*t) - 0.187989370184755*2.7183**(0.115*t) - 3.8925337880519e-16*2.7183**(0.119*t) + 2.57847628977542e-16*2.7183**(0.13*t) - 8.51716045044426e-32*2.7183**(0.145*t))/(5.21751626349937e-27*2.7183**(0.018*t) - 9.22450423897807e-12*2.7183**(0.029*t) + 4.81717898656887e-7*2.7183**(0.04*t) - 8.91839374320076e-12*2.7183**(0.044*t) + 9.62741308910494e-7*2.7183**(0.051*t) + 1.18680089316153e-6*2.7183**(0.055*t) - 2.89517451832862e-6*2.7183**(0.062*t) - 0.0366920278622904*2.7183**(0.066*t) + 1.77414681672507e-8*2.7183**(0.07*t) - 2.51222173116952e-10*2.7183**(0.073*t) - 0.13382672380572*2.7183**(0.077*t) - 0.00139504012928698*2.7183**(0.081*t) + 4.92771305482015e-27*2.7183**(0.084*t) - 1.87467005514554e-5*2.7183**(0.088*t) - 0.224201851026293*2.7183**(0.092*t) + 6.70335264048306e-8*2.7183**(0.096*t) - 6.66323425360142e-11*2.7183**(0.099*t) - 0.294297013296745*2.7183**(0.103*t) - 0.00527810445178314*2.7183**(0.107*t) - 1.68872917548782e-6*2.7183**(0.114*t) - 0.304343854126697*2.7183**(0.118*t) + 4.35817712240442e-18*2.7183**(0.122*t) - 1.74642628977799e-6*2.7183**(0.129*t) + 4.9555887867637e-16*2.7183**(0.133*t) - 2.56026053926774e-16*2.7183**(0.144*t) - 2.03821317827805e-31*2.7183**(0.148*t) + 2.97661289680374e-31*2.7183**(0.159*t) - 7.2271557760893e-47*2.7183**(0.174*t)) + 32326137136.4363*(-2.11551602296733e-23*2.7183**(0.018*t) + 3.74020617008673e-8*2.7183**(0.029*t) - 0.00195299556109448*2.7183**(0.04*t) + 3.61608932486681e-8*2.7183**(0.044*t) - 0.0142447199944637*2.7183**(0.051*t) - 0.00196243979485906*2.7183**(0.055*t) - 0.0259732677012158*2.7183**(0.062*t) - 0.0338602490164927*2.7183**(0.066*t) - 7.17989306968513e-5*2.7183**(0.07*t) - 2.25359885938225e-6*2.7183**(0.073*t) - 0.11492803917904*2.7183**(0.077*t) - 0.0195022232536778*2.7183**(0.081*t) + 4.42042530810686e-23*2.7183**(0.084*t) - 0.064008648763373*2.7183**(0.088*t) - 0.150600232165573*2.7183**(0.092*t) - 0.000543079614797581*2.7183**(0.096*t) - 5.97728175304011e-7*2.7183**(0.099*t) - 0.19617788538914*2.7183**(0.103*t) - 0.0613704198184755*2.7183**(0.107*t) - 0.0151494328534977*2.7183**(0.114*t) - 0.191806852930699*2.7183**(0.118*t) - 0.00102500163442383*2.7183**(0.122*t) - 0.0313334173574287*2.7183**(0.129*t) - 0.0593411863420975*2.7183**(0.133*t) - 0.0162023079651279*2.7183**(0.144*t) + 4.82260892409949e-17*2.7183**(0.148*t) + 1.11211671297216e-17*2.7183**(0.159*t) + 1.73169098882843e-33*2.7183**(0.174*t))/(6.19840932103725e-28*2.7183**(0.021*t) - 1.09587110359059e-12*2.7183**(0.032*t) + 5.72240903052018e-8*2.7183**(0.043*t) - 1.05950517669225e-12*2.7183**(0.047*t) + 3.2305386119673e-7*2.7183**(0.054*t) + 1.40983949906332e-7*2.7183**(0.058*t) + 7.31128022425865e-8*2.7183**(0.065*t) - 0.00435828296912597*2.7183**(0.069*t) + 2.10369080849743e-9*2.7183**(0.073*t) - 1.25421944653413e-6*2.7183**(0.076*t) - 0.0317931699316734*2.7183**(0.08*t) - 0.00016519137241584*2.7183**(0.084*t) - 1.08829445394264e-10*2.7183**(0.087*t) - 0.0579772609538318*2.7183**(0.091*t) - 0.0436782366103658*2.7183**(0.095*t) + 2.13468529534809e-27*2.7183**(0.098*t) + 1.59120976155655e-8*2.7183**(0.099*t) - 8.12119114711745e-6*2.7183**(0.102*t) - 0.192043640899425*2.7183**(0.106*t) - 0.0012520142419818*2.7183**(0.11*t) - 2.88651307866013e-11*2.7183**(0.113*t) - 0.127498065659054*2.7183**(0.117*t) - 0.138889211941493*2.7183**(0.121*t) + 3.00322929071134e-8*2.7183**(0.125*t) - 7.31587331376235e-7*2.7183**(0.128*t) - 0.263692616225766*2.7183**(0.132*t) - 0.00236469103430803*2.7183**(0.136*t) - 1.5131346111028e-6*2.7183**(0.143*t) - 0.136351826640535*2.7183**(0.147*t) + 1.95254611980909e-18*2.7183**(0.151*t) - 7.82432145447249e-7*2.7183**(0.158*t) + 2.22019789127495e-16*2.7183**(0.162*t) - 1.14704534516248e-16*2.7183**(0.173*t) - 9.13158212898649e-32*2.7183**(0.177*t) + 1.33357910855661e-31*2.7183**(0.188*t) - 3.23790304329666e-47*2.7183**(0.203*t)) )
  dydt = 0.00810098*x + 0.01550481*y + 0.00982069*z
  dzdt = 0.02406615*x + 0.00679688*y + 0.01145372*z
  #dXdt = [dx1dt,dx2dt,...dxndt]
  dudt = [dxdt,dydt,dzdt]
  return dudt
#x1(0)=...,x2(0)=...,xn(0)=...
X0=[3823518.3,11922242.2,18063252.8]
t = np.linspace(0,1,50)
sol = odeint(f2,X0,t,tfirst=True)

print("x_1 =  \n",sol[:,0].tolist(),"\n")
print("x_2 =  \n",sol[:,1].tolist(),"\n")
print("x_3 =  \n",sol[:,2].tolist(),"\n")


#创建画板1
fig = plt.figure(1) #如果不传入参数默认画板1
ax1=plt.subplot(3,1,1)  #创建画纸，并选择画纸1 
plt.plot(t,sol[:,0],"k-")#在画纸1上绘图

ax2=plt.subplot(3,1,2) #选择画纸2
plt.plot(t,sol[:,1],"k-")#在画纸2上绘图

ax3=plt.subplot(3,1,3) #选择画纸3
plt.plot(t,sol[:,2],"k-")#在画纸3上绘图
#显示图像
plt.show()

# #创建画板2
# fig = plt.figure(2) #如果不传入参数默认画板1
# plt.plot(t,sol[:,0],"k-")#在画纸1上绘图
# plt.plot(t,sol[:,1],"k-")#在画纸2上绘图
# plt.plot(t,sol[:,2],"k-")#在画纸3上绘图
# #显示图像
# plt.show()