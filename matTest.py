
import os

import matplotlib.pyplot as plt


# 画板
fig = plt.figure()

# 纸张
ax = fig.add_subplot(111)

# 绘制图形
ax.set(xlim=[0.5, 5.5], ylim=[-2,8], xlable='人设', ylabel='指数', title='人设测试结果')

# 显示
plt.show()
