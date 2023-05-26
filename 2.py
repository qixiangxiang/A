import matplotlib.pyplot as plt

# 创建数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建画布和子图
fig, ax = plt.subplots()

# 绘制线条
ax.plot(x, y)

# 添加标题和坐标轴标签
ax.set_title('简单图示')
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')

# 显示图像
plt.show()
