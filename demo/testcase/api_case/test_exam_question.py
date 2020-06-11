import unittest
import utx
from utx import log


class ExamQurwstion(unittest.TestCase):
    def test_1(self):
        """字符串中找出相同元素并按照频率排序"""
        s = "1176546399ggcjsjbuishdsdbhcguydgsjvc676734573587hudgfhwjgfsgkjihjghjggsdjgfj6868"
        di = {
            key: s.count(key) for key in set((s))
        }
        print(di)
        # 倒叙排序字典
        dic = sorted(di.items(), key=lambda key: key[1], reverse=True)
        print(dic)
        log.info("字符串中找出相同元素并按照频率排序成功")

    def test_2(self):
        """把列表里边相加为10 的数字打印出来"""
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111, 22, 3, 5, 6, 7]
        list1 = []
        list2 = []
        for i in list:
            for k in list:
                if i not in list1:
                    if i + k == 10:
                        print((i, k))
                        list2.append((i, k))
                        list1.append(k)
        print(list2)
        list3 = set(list2)
        print(list3)
        log.info("把列表里边相加为10 的数字打印出来")


