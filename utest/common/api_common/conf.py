# encoding: utf-8
import configparser
import os

project_path = os.path.dirname(os.path.dirname(__file__))
# 基础路径
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
# 导出、下载文件目录
export_path = project_path + '/file/export'
# 导入文件目录
template_path = project_path + '/file/template'


# 获取单个配置信息
def get_config(target_section, target_option):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(project_path, 'config/conf.ini'), encoding='utf-8')
    r = cf.get(target_section, target_option)
    return r


# 获取单节配置信息
def get_config_section(target_section):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(project_path, 'config/conf.ini'), encoding='utf-8')
    return cf.items(target_section)


# 更新配置信息
def update_config(target_section, target_option, target_value):
    # 读取配置文件
    cf = configparser.ConfigParser()
    cf.read(os.path.join(project_path, 'config/conf.ini'), encoding='utf-8')
    # 更新配置文件
    cf.set(target_section, target_option, target_value)
    # 循环写入
    with open(os.path.join(project_path, 'config/conf.ini'), 'w', encoding='utf-8') as fw:
        cf.write(fw)


# 标签/项目联系信息
tag_contact = {
    'admin': {'users': 'lidongdong,hancheng', 'wx_robot_address': ''},
    'test': {'users': 'lidongdong,hancheng', 'wx_robot_address': ''},
    'base': {'users': 'lidongdong,hancheng', 'wx_robot_address': ''},
    'flow': {'users': 'all', 'wx_robot_address': ''},
    'smoke': {'users': 'all', 'wx_robot_address': ''},
    'agent': {'users': 'yangwenxue', 'wx_robot_address': ''},
    'autoquery': {'users': 'zhangjian,guobaohui', 'wx_robot_address': ''},
    'bidding': {'users': 'wanghairui', 'wx_robot_address': ''},
    'bms': {'users': 'sunzhuye', 'wx_robot_address': ''},
    'customer': {'users': 'liqi', 'wx_robot_address': ''},
    'dispatch': {'users': 'wanghairui', 'wx_robot_address': ''},
    'driver': {'users': 'liuxiongjin,gaopenghong,guobingjie', 'wx_robot_address': ''},
    'energy': {'users': 'liqi', 'wx_robot_address': ''},
    'finance': {'users': 'lidongdong,shanxinxin,wuxiuxiu,shenyuhui,wangxueqin,huangpeng,zuolin,yuanfangyan',
                'wx_robot_address': 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=577b6c52-be22-44e0-9ef2-70a4c74a372a'},
    'newton': {'users': 'yangwenxue', 'wx_robot_address': ''},
    'oil': {'users': 'gaowei', 'wx_robot_address': ''},
    'oms': {'users': 'wangtingting', 'wx_robot_address': ''},
    'service': {'users': 'yinqiang', 'wx_robot_address': ''},
    'third': {'users': 'zhangjian,guobaohui', 'wx_robot_address': ''},
    'truck': {'users': 'hancheng', 'wx_robot_address': ''},
    'turing': {'users': 'wanghairui', 'wx_robot_address': ''},
    'im': {'users': 'gaowei', 'wx_robot_address': ''},
    'erobot': {'users': 'gaowei', 'wx_robot_address': ''},
    'foryou': {'users': 'liuxiongjin', 'wx_robot_address': ''}
}

# 测试人员信息
user_info = {
    'liuchunfu': {'name': '刘春福', 'mobile': '18515579500'},
    'lidongdong': {'name': '李东东', 'mobile': '13121768752'},
    'shanxinxin': {'name': '单欣欣', 'mobile': '18310179572'},
    'wuxiuxiu': {'name': '吴秀秀', 'mobile': '18600561346'},
    'wangxueqin': {'name': '王雪芹', 'mobile': '18911487112'},
    'shenyuhui': {'name': '沈玉会', 'mobile': '13718726993'},
    'zhangjian': {'name': '张健', 'mobile': '18601965979'},
    'yinqiang': {'name': '殷强', 'mobile': '15944584448'},
    'sunzhuye': {'name': '孙竹叶', 'mobile': '17313157107'},
    'guobaohui': {'name': '郭宝慧', 'mobile': '13366863847'},
    'hancheng': {'name': '韩程', 'mobile': '15901219897'},
    'wanghairui': {'name': '王海瑞', 'mobile': '15010032693'},
    'wangtingting': {'name': '王婷婷', 'mobile': '17710722656'},
    'duxin': {'name': '杜鑫', 'mobile': '18612320149'},
    'yangwenxue': {'name': '杨文学', 'mobile': '18301556584'},
    'liqi': {'name': '李琦', 'mobile': '18514587147'},
    'guobingjie': {'name': '郭冰洁', 'mobile': '18334704870'},
    'gaopenghong': {'name': '高鹏鸿', 'mobile': '18636299591'},
    'liuxiongjin': {'name': '柳雄金', 'mobile': '13121757718'},
    'zhaixiaohao': {'name': '翟小皓', 'mobile': '13718255823'},
    'gaowei': {'name': '高伟', 'mobile': '18310860962'},
    'huoaimei': {'name': '霍爱梅', 'mobile': '15545055217'},
    'liangyu': {'name': '梁雨', 'mobile': '13120327312'},
    'linyuxiu': {'name': '林玉秀', 'mobile': '18276709611'},
    'lisu': {'name': '黎素', 'mobile': '18276705311'},
    'yangshuli': {'name': '杨术丽', 'mobile': '13074579832'},

    'zhaolibin': {'name': '赵利斌', 'mobile': '18500061604'},
    'xuxiaolong': {'name': '徐晓龙', 'mobile': '15311074577'},
    'wangqi': {'name': '王旗', 'mobile': '13121911105'},
    'fanweiqiang': {'name': '范伟强', 'mobile': '18642802671'},
    'bidong': {'name': '毕冬', 'mobile': '17600974689'},
    'duyouwei': {'name': '杜有卫', 'mobile': '16601117820'},
    'xingxun': {'name': '邢迅', 'mobile': '15210931498'},
    'xiezhijie': {'name': '谢治杰', 'mobile': '13261995529'},
    'guopenghui': {'name': '郭鹏辉', 'mobile': '15501206180'},
    'chenjiwu': {'name': '陈集武', 'mobile': '18512820932'},
    'yuanruixia': {'name': '原瑞霞', 'mobile': '17778013554'},
    'xieqitao': {'name': '谢启涛', 'mobile': '15001298279'},
    'wuhaitao': {'name': '武海涛', 'mobile': '13011108440'},
    'zhangmeichan': {'name': '张妹蝉', 'mobile': '15313274097'},
    'qiutiangang': {'name': '邱天罡', 'mobile': '18743432166'},
    'xieqiuying': {'name': '谢秋颖', 'mobile': '18945225950'},
    'jiachengquan': {'name': '贾承权', 'mobile': '17611686796'},
    'cuidong': {'name': '崔东', 'mobile': '13720606714'},
    'liujinhao': {'name': '刘进浩', 'mobile': '18513581958'},
    'lijuan': {'name': '李娟', 'mobile': '15210955615'},
    'wanghao': {'name': '王浩', 'mobile': '15011303093'},
    'zhouchao': {'name': '周超', 'mobile': '13699129630'},
    'chenguoan': {'name': '陈国安', 'mobile': '17600382098'},
    'jiangwenping': {'name': '蒋文平', 'mobile': '13520038524'},
    'zhouzeyang': {'name': '周泽洋', 'mobile': '17512526627'},
    'yangtong': {'name': '杨通', 'mobile': '15614122498'},
    'pengcun': {'name': '彭存', 'mobile': '15910925214'},
    'liuhongjun': {'name': '刘洪军', 'mobile': '13366775587'},
    'yixingjun': {'name': '伊兴君', 'mobile': '18910653004'},
    'lilimin': {'name': '李立敏', 'mobile': '15810554635'},
    'wangxin': {'name': '王鑫', 'mobile': '18334705826'},
    'sunjie': {'name': '孙杰', 'mobile': '18735973395'},
    'liuyoushen': {'name': '刘友申', 'mobile': '13264200806'},
    'wangxiangyu': {'name': '王向禹', 'mobile': '13661079917'},
    'liweiping': {'name': '李伟平', 'mobile': '15313591050'},

    'huangpeng': {'name': '黄鹏', 'mobile': '13330270717'},
    'zuolin': {'name': '左琳', 'mobile': '15733672776'},
    'yuanfangyan': {'name': '袁方言', 'mobile': '15116900732'},
}

if __name__ == '__main__':
    pass
    from xpinyin import Pinyin

    users = ['黄鹏|13330270717', '左琳|15733672776', '袁方言|15116900732']
    for user in users:
        user_detail = user.split('|')
        user_name = user_detail[0]
        user_mobile = user_detail[1]
        print('\'%s\': {\'name\': \'%s\', \'mobile\': \'%s\'},' % (
            Pinyin().get_pinyin(user_name).replace('-', ''), user_name, user_mobile))
