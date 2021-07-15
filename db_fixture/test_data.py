import sys

sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    # 't_': [
    #     {'id': '40288a4867e9c88c0167e9e1b6f10094', 'order_no': '123', 'user_id': '123', 'licenset_plate_id': '123',
    #      'parking_id': '123',
    #      'total_money': '1', 'scheduled_time': '2018-12-18 15:16:08', 'settlement_time': '2018-12-28 15:14:28',
    #      'parking_time': '14398', 'wallet_pay_no': 'null', 'wallet_pay_money': '0.01', 'wei_pay_no': 'null',
    #      'wei_pay_money': '0.01',
    #      'ali_pay_no': 'null', 'ali_pay_money': '0.01', 'order_status': '1', 'update_time': '2019-02-13 15:03:25',
    #      'create_time': '2019-02-13 15:03:25'
    #      }
    #
    # ],
    # 't_user': [
    #     {'id': '17600116141', 'user_name': 'alen', 'nick_name': '17600116141',
    #      'password': '0pmP9oshZLwOcoP7EbwSgQ==', 'phone': '17600116141', 'email': 'alen@mail.com', 'sign': 0,
    #      'event_id': 1}
    # ]
}


def init_data():
    DB().init_data(datas)
    # DB().update('t_login')


if __name__ == '__main__':
    init_data()
