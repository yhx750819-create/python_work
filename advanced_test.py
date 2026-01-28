# 测试1: 基础语法和数学运算
print("=== 测试1: 基础运算 ===")
result = (5 + 3) * 2
print(f"运算结果 (5+3)*2 = {result}")
assert result == 16, "基础运算测试失败！"

# 测试2: 列表和循环
print("\n=== 测试2: 列表与循环 ===")
fruits = ["苹果", "香蕉", "橙子"]
for i, fruit in enumerate(fruits, 1):
    print(f"水果 {i}: {fruit}")
assert len(fruits) == 3, "列表测试失败！"

# 测试3: 使用pip安装的第三方库 (以requests为例)
print("\n=== 测试3: 尝试导入第三方库 ===")
try:
    # 注意：运行前需要在终端安装：pip install requests
    import requests
    print("✅ 成功导入 'requests' 库！")
    print("   你可以用它来访问网页。")
except ImportError:
    print("⚠️  'requests' 库未安装。")
    print("   你可以在终端输入: pip install requests 来安装它。")

# 测试4: 文件操作
print("\n=== 测试4: 文件读写 ===")
test_filename = "test_write.txt"
with open(test_filename, 'w', encoding='utf-8') as f:
    f.write("这是一个Python创建的测试文件。\nHello, World!")

with open(test_filename, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"已成功创建并读取文件 '{test_filename}'")
    print(f"文件内容预览: {content[:30]}...")

import os
os.remove(test_filename)  # 清理测试文件
print(f"已清理测试文件。")

print("\n" + "="*40)
print("🎉 所有基础测试通过！你的Python环境工作正常。")
print("="*40)