# 导入必要的模块
import numpy as np
import matplotlib.pyplot as plt

# 产生测试数据
x = np.arange(1, 10)
print("x:"+str(x))
y = np.arange(10, 1, -1)
print("y:"+str(y))
fig = plt.figure()
ax1 = fig.add_subplot(111)
# 设置标题
ax1.set_title('Scatter Plot')
# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y')
sValue = x*50
print("s:"+str(sValue))
# 画散点图
cValue = ['r', 'y', 'g', 'b', 'r', 'y', 'g', 'b', 'r']
ax1.scatter(x, y, s=sValue, c=cValue, marker='s')
# 设置图标
plt.legend('x1')
# 显示所画的图
plt.show()