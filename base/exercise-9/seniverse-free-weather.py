import requests

import json_util

weather_data={}

# 查询天气实况
def get_weather(city:str):
    url = "https://api.seniverse.com/v3/weather/now.json"
    params = {
        "key": "SIKAtSLBNAYO6FdVJ",
        "location": city,
        "language": "zh-Hans",
        "unit": "c"
    }
    weather = json_util.json_to_dict(requests.get(url, params=params).text)
    for result in weather['results']:
        city_name = result.get('location').get('name')
        if weather_data.get(city_name) is None:
            weather_data[city_name]={}
        weather_data[city_name]['now'] = result['now']
        weather_data[city_name]['last_update'] = result['last_update']


# 查询未来三天天气
def get_daily(city:str):
    url = "https://api.seniverse.com/v3/weather/daily.json"
    params = {
        "key": "SIKAtSLBNAYO6FdVJ",
        "location": city,
        "language": "zh-Hans",
        "unit": "c",
        "start":0,
        "end":3
    }
    daily = json_util.json_to_dict(requests.get(url, params=params).text)
    for result in daily['results']:
        city_name = result.get('location').get('name')
        if weather_data.get(city_name) is None:
            weather_data[city_name]={}
        weather_data[city_name]['daily'] = result['daily']


# 查询生活指数
def get_suggestion(city:str):
    url = "https://api.seniverse.com/v3/life/suggestion.json"
    params = {
        "key": "SIKAtSLBNAYO6FdVJ",
        "location": city,
        "language": "zh-Hans",
        "days": "5"
    }
    suggestion = json_util.json_to_dict(requests.get(url, params=params).text)
    for result in suggestion['results']:
        city_name = result.get('location').get('name')
        if weather_data.get(city_name) is None:
            weather_data[city_name]={}
        weather_data[city_name]['suggestion'] = result['suggestion']

def print_weather_info():
    for city, data in weather_data.items():
        print("截至{},{}的天气为{}、温度为{}度，未来三天的天气情况如下：".format(data['last_update'],city, data['now']['text'],data['now']['temperature']))
        for day in data['daily']:
            date = day['date']
            text_day = day['text_day']
            code_day = day['code_day']
            text_night = day['text_night']
            code_night = day['code_night']
            high = day['high']
            low = day['low']
            rainfall = day['rainfall']
            precip = day['precip']
            wind_direction = day['wind_direction']
            wind_direction_degree = day['wind_direction_degree']
            wind_speed = day['wind_speed']
            wind_scale = day['wind_scale']
            humidity = day['humidity']

            print(f"日期：{date}")
            print(f"白天天气：{text_day}（代码：{code_day}）")
            print(f"夜间天气：{text_night}（代码：{code_night}）")
            print(f"温度：最高：{high}°C，最低：{low}°C")
            print(f"降雨量：{rainfall} 毫米")
            print(f"降水概率：{precip}%")
            print(f"风向：{wind_direction}（{wind_direction_degree}°），风速：{wind_speed} 公里/小时，风力：{wind_scale}")
            print(f"湿度：{humidity}%")
            print()

        for suggestion in data['suggestion']:
            date = suggestion['date']
            print(f"日期：{date}")
            for index, details in suggestion.items():
                if index != 'date':
                    index_brief = details['brief']
                    index_details = details['details']
                    print(f"{index}指数：{index_brief}")
                    print(f"{index}详情：{index_details}")
                    print()

                    print(f"日期：{date}")

# 查询心知天气
def get_heart(city:str):
    get_weather(city)
    get_daily(city)
    get_suggestion(city)
    print_weather_info()

if __name__ == '__main__':
    get_heart('shenzhen')