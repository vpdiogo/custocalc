tariff_values = [
    {
        "origin": 11,
        "destination": 16,
        "value": 1.9
    },
    {
        "origin": 16,
        "destination": 11,
        "value": 2.9
    },
    {
        "origin": 11,
        "destination": 17,
        "value": 1.7
    },
    {
        "origin": 17,
        "destination": 11,
        "value": 2.7
    },
    {
        "origin": 11,
        "destination": 18,
        "value": 0.9
    },
    {
        "origin": 18,
        "destination": 11,
        "value": 1.9
    },
]


import locale

def currency(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    value = locale.currency(value, grouping=True, symbol=None)
    return value

def calculate_without_plan(origin, destination, time):

    for item in tariff_values:
        if origin == item["origin"] and destination == item["destination"]:
            value = item["value"] * time

            return currency(value)
        
    return "-"

def calculate_plan_30(origin, destination, time):

    for item in tariff_values:
        if origin == item["origin"] and destination == item["destination"]:
            if time > 30:
                value = item["value"] * (time - 30) * 1.1
                return currency(value)
            else:
                return 0
    return "-"

def calculate_plan_60(origin, destination, time):

    for item in tariff_values:
        if origin == item["origin"] and destination == item["destination"]:
            if time > 60:
                value = item["value"] * (time - 60) * 1.1
                return currency(value)
            else:
                return 0
    return "-"

def calculate_plan_120(origin, destination, time):

    for item in tariff_values:
        if origin == item["origin"] and destination == item["destination"]:
            if time > 120:
                value = item["value"] * (time - 120) * 1.1
                return currency(value)
            else:
                return 0
    return "-"