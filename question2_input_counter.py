# -*- coding: utf-8 -*-
# @Time    :2023/6/10 4:40
# @Author  :lzh
# @File    : question2_input_counter.py
# @Software: PyCharm
def get_input():
    """获取用户输入的整数，直到用户输入'q'为止"""
    while True:
        num = input("请输入一个整数（输入'q'退出）：")
        if num == 'q':
            return
        try:
            yield int(num)
        except ValueError:
            print("仅支持整型输入")


def process_numbers():
    """统计用户输入的整数"""
    negative_count = 0
    non_negative_sum = 0
    non_negative_count = 0

    for num in get_input():
        if num < 0:
            negative_count += 1
        else:
            non_negative_sum += num
            non_negative_count += 1

    avg = non_negative_sum / non_negative_count if non_negative_count else 0

    print(f"负数的数量：{negative_count}\n非负数的平均值：{avg}")


if __name__ == '__main__':
    process_numbers()
