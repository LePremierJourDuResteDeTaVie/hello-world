# -*- coding: utf-8 -*-
#下面这两行，应该是申明的意思，就是说，要用到这两库中的函数，可以暂时不看
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.28, 1000)#这个函数有三个参数，0和6.28（等于2π）表示x的取值范围，1000表示有1000的点，越多，图形越精确
y = np.sin(x)#y=sinx，就是数学函数
z = np.sin(x*3)#同上

#plt.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
#fill这个是填充颜色的指令，如果只是画线，可以用下面的plot。
plt.fill(x, y, 'b', x, z, 'r', alpha=0.5)#绘图指令，就是关键的一行，x，y，z是上面的几个值，b、r表示颜色，蓝和红，alpha貌似是对比度，暂时没搞清楚。。。。
# plt.figure(figsize=(12,6))#这个是图的大小，应该可以不用，有默认的。
# plt.plot(x,y,label="$sin(x)$",color="red",linewidth=1)
# plt.plot(x,z,"b",label="$cos(x^2)$")
plt.xlabel("Time(s)")#x轴的坐标说明，双引号部分可以随意修改
plt.ylabel("Volt")#同上，变味Y轴
plt.title("PyPlot First Example")#图的标题，同上
plt.ylim(-1.0,1.0)#Y轴的取值范围
# plt.legend()
plt.show()