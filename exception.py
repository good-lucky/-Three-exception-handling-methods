
# raise
def make_raise(n):
    # 假设n必须是 0~100之间的数
    print("begin...")
    if n > 100:  # 传过的来参数无效，怎么告诉调用者呢？
        raise ValueError
    if n < 0:
        raise ValueError("参数小于零错误:%d" % n)
    print("end")



#  assert
def get_age():
    a = input("请输入年龄：")
    a = int(a)
    assert a < 140, "年龄不可能大于140!!!"
    assert a >= 0, "年龄不可能出现负数!!!"
    return a




try:
	# 可能会发生异常的语句
except Exception as e:

