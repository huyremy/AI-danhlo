from sklearn.linear_model import LinearRegression

# Chuỗi số ban đầu
numbers = [00, 97, 92, 48, 00, 52, 10, 39, 49, 55, 75, 98, 69, 7, 87, 98, 98, 2, 43, 14, 66, 14, 53, 36, 97, 41, 57]

X_train = [[numbers[i]] for i in range(len(numbers)-1)]
y_train = [numbers[i] for i in range(1, len(numbers))]

# Huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán số thứ 28
number_28 = model.predict([[numbers[-1]]])
print("Dự đoán số ngày mai là:", int(number_28))
