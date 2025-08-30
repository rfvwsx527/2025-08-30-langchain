# Python變數與數學運算

## 1. 變數 (Variables)

在Python中，變數用於儲存資料值。你可以將任何資料類型（數字、字串、列表等）賦值給變數。

### 變數命名規則:
- 變數名稱可以包含字母、數字和底線。
- 變數名稱不能以數字開頭。
- 變數名稱區分大小寫 (`myVar` 和 `myvar` 是不同的變數)。
- 避免使用Python的保留字 (如 `if`, `for`, `while`, `class` 等) 作為變數名稱。

### 宣告和賦值:
```python
# 宣告一個整數變數
x = 10

# 宣告一個浮點數變數
y = 3.14

# 宣告一個字串變數
name = "Alice"

# 宣告一個布林變數
is_student = True

print(x)        # 輸出: 10
print(y)        # 輸出: 3.14
print(name)     # 輸出: Alice
print(is_student) # 輸出: True
```

## 2. 數學運算 (Mathematical Operations)

Python支援多種數學運算符，可以對數字進行加、減、乘、除等操作。

### 基本運算符:

| 運算符 | 描述     | 範例        | 結果 |
|--------|----------|-------------|------|
| `+`    | 加法     | `5 + 2`     | `7`  |
| `-`    | 減法     | `5 - 2`     | `3`  |
| `*`    | 乘法     | `5 * 2`     | `10` |
| `/`    | 除法     | `5 / 2`     | `2.5`|
| `//`   | 整數除法 | `5 // 2`    | `2`  |
| `%`    | 取餘數   | `5 % 2`     | `1`  |
| `**`   | 冪次運算 | `5 ** 2`    | `25` |

### 範例:
```python
a = 10
b = 3

# 加法
sum_result = a + b
print(f"加法: {a} + {b} = {sum_result}") # 輸出: 加法: 10 + 3 = 13

# 減法
diff_result = a - b
print(f"減法: {a} - {b} = {diff_result}") # 輸出: 減法: 10 - 3 = 7

# 乘法
prod_result = a * b
print(f"乘法: {a} * {b} = {prod_result}") # 輸出: 乘法: 10 * 3 = 30

# 除法
div_result = a / b
print(f"除法: {a} / {b} = {div_result}") # 輸出: 除法: 10 / 3 = 3.333...

# 整數除法
floor_div_result = a // b
print(f"整數除法: {a} // {b} = {floor_div_result}") # 輸出: 整數除法: 10 // 3 = 3

# 取餘數
mod_result = a % b
print(f"取餘數: {a} % {b} = {mod_result}") # 輸出: 取餘數: 10 % 3 = 1

# 冪次運算
pow_result = a ** b
print(f"冪次運算: {a} ** {b} = {pow_result}") # 輸出: 冪次運算: 10 ** 3 = 1000
```

### 運算順序 (Order of Operations):
Python 遵循數學上的運算順序（PEMDAS/BODMAS）：
1. 括號 (Parentheses)
2. 冪次 (Exponents)
3. 乘法、除法、整數除法、取餘數 (Multiplication, Division, Floor Division, Modulo) - 由左至右
4. 加法、減法 (Addition, Subtraction) - 由左至右

範例:
```python
result = 10 + 5 * 2 - (6 / 3) ** 2
# 步驟 1: (6 / 3) = 2.0
# 步驟 2: 2.0 ** 2 = 4.0
# 步驟 3: 5 * 2 = 10
# 步驟 4: 10 + 10 = 20
# 步驟 5: 20 - 4.0 = 16.0

print(result) # 輸出: 16.0
```
