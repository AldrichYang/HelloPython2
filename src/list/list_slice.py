# -*- coding: utf-8 -*-

# 根据分片尺寸把一个数组分片


def slice_list(orig_list, slice_size=10):
    slice_parts = len(orig_list) / slice_size
    remainder = len(orig_list) % slice_size
    index = 0
    slices = []
    if slice_parts == 0:
        slices.append(orig_list)
    else:

        while index < slice_parts:
            each_part = orig_list[index * slice_size:(index + 1) * slice_size]
            index += 1
            slices.append(each_part)
        if remainder > 0:
            slices.append(orig_list[slice_parts*slice_size:len(orig_list)])
    return slices


# 测试代码
if __name__ == '__main__':
    test_lists = [2]*14
    slice_lists = slice_list(test_lists, 6)
    for each in slice_lists:
        print ','.join(map(str, each))