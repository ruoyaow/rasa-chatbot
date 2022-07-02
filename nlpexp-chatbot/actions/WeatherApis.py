# -*- coding: utf-8 -*-

# 使用心知天气数据查询天气

import requests
import json

KEY = 'rmhrne8hal69uwyv'  # API key
UID = ""

LOCATION = 'beijing'
API = 'https://api.seniverse.com/v3/weather/daily.json'  # API URL
UNIT = 'c'
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言


def fetch_weather(location, start=0, days=15):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT,
        'start': start,
        'days': days
    }, timeout=2)
    return result.json()


def get_weather_by_day(location, day=1):
    result = fetch_weather(location)
    normal_result = {
        "location": result["results"][0]["location"],
        "result": result["results"][0]["daily"][day]
    }

    return normal_result


if __name__ == '__main__':
    default_location = "合肥"
    result = fetch_weather(default_location)
    print(json.dumps(result, ensure_ascii=False))

    default_location = "兰州"
    result = get_weather_by_day(default_location)
    print(json.dumps(result, ensure_ascii=False))
