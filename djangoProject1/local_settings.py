# -*- codeing = utf-8 -*-
# @Time:2023/7/30 15:20
# @Author:lhx
# @File:local_settings.py
# @Software:PyCharm


# 腾讯云短信应用的app_id
TENCENT_SMS_APP_ID=1400843623
# 腾讯云短信应用的app_key
TENCENT_SMS_APP_KEY='4488e79c13bbb907568fa0b261517177'

# 腾讯云短信签名内容
TENCENT_SMS_SIGN='脑洞打开公众号'


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/0", # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            # "PASSWORD": "foobared" # redis密码foobared
        },
    },
}