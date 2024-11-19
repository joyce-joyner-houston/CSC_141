from city_functions import city_country

def test_city_country():
    result = city_country('philadephia', 'united states')
    assert result == 'Philadelphia, United States'
