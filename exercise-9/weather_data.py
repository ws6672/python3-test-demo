class WeatherData:
    def __init__(self, results):
        self.results = results

class Location:
    def __init__(self, id, name, country, path, timezone, timezone_offset):
        self.id = id
        self.name = name
        self.country = country
        self.path = path
        self.timezone = timezone
        self.timezone_offset = timezone_offset

class Weather:
    def __init__(self, text, code, temperature):
        self.text = text
        self.code = code
        self.temperature = temperature

class WeatherInfo:
    def __init__(self, location, now, last_update, timezone_offset):
        self.location = location
        self.now = now
        self.last_update = last_update
        self.timezone_offset = timezone_offset
