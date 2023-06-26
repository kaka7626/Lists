age = [10, 20, 30]
age[1] = 'Long' #thay đổi giá trị item trong danh sách
print(age)

age[1:3] = ['poor ass', 'not handsome', 'degenerate'] # cắt (slice) lấy item bắt đầu từ item 1, không bao gồm 3
print(age)

print(age[:2]) #python bắt đầu từ item 0
print(age[0:]) #python lấy hết các item còn lại