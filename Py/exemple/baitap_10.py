#Viết chương trình Python in cây thông ra màn hình theo mẫu
# Xác định chiều cao của cây thông
height = 5

# Vòng lặp để vẽ phần thân cây
for i in range(height):
    # In khoảng trắng để căn giữa
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Vòng lặp để vẽ phần gốc cây
print(" " * (height - 1) + "*")

#này thử sài f-string (formatted string literals) á
# Xác định chiều cao của cây thông
height = 5

# Vẽ phần thân cây
for i in range(height):
    stars = '*' * (2 * i + 1)
    print(f"{stars:^{2*height-1}}")  # Căn giữa theo chiều rộng

# Vẽ phần gốc cây
print(f"{'*':^{2*height-1}}")