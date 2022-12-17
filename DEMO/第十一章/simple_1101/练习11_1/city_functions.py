def city_country(city, country, population=0):  # int型变量格式，不能直接population
    """返回一个城市名和一个国家名"""
    if population:
        string = f"{city.title()} , {country.title()}-population {population}"
    else:
        string = f"{city.title()} , {country.title()}"
    return string
