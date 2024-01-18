target={
    'TF0401':{
        'starttime':'09:25:00',
        'openpr':0, #0 根据集合竞价动态，非0 手工指定价格
        'sell':{
            'from':5,
            'to':10,
            'split':1,
            'vol':1,
        },
        'buy': {
            'from': 5,
            'to': 10,
            'split': 1,
            'vol': 1,
        },
        'tick': 50, #最小跳动价格
        'close':1,  #平仓挂单加多少tick
        'limit':10, #按多少个tick止损
    },
}

# SimNow 提供的四个环境
simnow={
    "fronts": {
        "7x24": {
            "td": "tcp://180.168.146.187:10130",
            "md": "tcp://180.168.146.187:10131",
        },
        "电信": {
            "td": "tcp://180.168.146.187:10202",
            "md": "tcp://180.168.146.187:10212",
        },
        "移动": {
            "td": "tcp://218.202.237.33:10203",
            "md": "tcp://218.202.237.33:10213",
        },
    },
    # 投资者ID / 密码
    "user": "119396",
    "password": "simnow@123",

    # 以下为连接 SimNow 环境的固定值
    "broker_id": "9999",
    "authcode": "0000000000000000",
    "appid": "simnow_client_test",
}
# GF
gf={
    "fronts": {
        "电信": {
            "td": "tcp://61.140.230.180:51205",
            "md": "tcp://61.140.230.180:51213",
        },
        "联通": {
            "td": "tcp://58.248.23.189:51205",
            "md": "tcp://58.248.23.189:51213",
        },
    },
    # 投资者ID / 密码
    "user": "xxx",
    "password": "xxx",

    # 以下为连接 SimNow 环境的固定值
    "broker_id": "9999",
    "authcode": "0000000000000000",
    "appid": "simnow_client_test",
}



