# —*- coding:utf-8 -*-
# Created by Administrator on 2020/6/6
# Copyright (C) 2020 $USER.All rights reserved.
import requests


def get_room():
    params = {
        "roomId": "5edb59def058f456c2b3dae5",
        "language": "zh",
        "access_token": "56bf7ef035f94e96b13849af8457ae57",
        "salt": "1591696330821",
        "secret": "uunlKo%2B%2B0mt1wbeVGhK%2Fzw%3D%3D"
    }
    url = "http://121.89.182.48:8094/room/getRoom?"
    re = requests.get(url=url, params=params)
    print(re.json())

def ddd():
    url = "http://121.89.182.48:8094/room/get?pageSize=50&roomId=5edb59def058f456c2b3dae5&language=zh&access_token=56bf7ef035f94e96b13849af8457ae57&salt=1591696330818&secret=uvbQEhie0qifsuZ9NZRaWw%3D%3D"
if __name__ == '__main__':
    get_room()
