import requests
import json

def from_json_string(json_string:str, class_name:str):
    return json.loads(json_string, object_hook=lambda d: namedtuple(class_name, d.keys())(*d.values()))

# 查询天气实况
def get_weather(city:str):
    url = "https://api.seniverse.com/v3/weather/now.json"
    params = {
        "key": "SIKAtSLBNAYO6FdVJ",
        "location": city,
        "language": "zh-Hans",
        "unit": "c"
    }
    response = requests.get(url, params=params)
    print(response)

# 查询未来三天天气
def get_forecast(city:str):
    url = "https://api.seniverse.com/v3/weather/daily.json"
    params = {
        "key": "SIKAtSLBNAYO6FdVJ",
        "location": city,
        "language": "zh-Hans",
        "unit": "c",
        "start":0,
        "end":3
    }
    response = requests.get(url, params=params)
    print(response)

# 查询生活指数
def get_suggestion(city:str):
    url = "https://api.seniverse.com/v3/life/suggestion.json"
    params = {
        "key": "SIKAtSLBNAYO6FdVJ",
        "location": city,
        "language": "zh-Hans",
        "days": "5"
    }
    response = requests.get(url, params=params)
    print(response)

# 查询心知天气
def get_heart(city:str):
    get_forecast(city)
    get_weather(city)
    get_suggestion(city)


if __name__ == '__main__':
    get_heart('shanghai')