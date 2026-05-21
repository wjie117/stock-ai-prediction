# predict.py
# 这是一个简单的股票趋势预测示例（AI入门版）

import numpy as np
from sklearn.linear_model import LinearRegression

# 模拟股票数据：过去5天的收盘价
# X 是输入（天数），y 是输出（价格）
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([100, 102, 105, 107, 110])

# 创建 AI 模型
model = LinearRegression()

# 训练模型（让 AI 学习规律）
model.fit(X, y)

# 预测第6天的价格
next_day = np.array([[6]])
predicted_price = model.predict(next_day)

print(f"AI 预测第6天的股票价格是: {predicted_price[0]:.2f} 元")
