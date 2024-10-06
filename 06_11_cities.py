cities = {'New York': {
        'country': 'United States',
        'population': 19469200,
        'fact': 'Known as the Big Apple.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 37115000,
        'fact': 'Famous for its cherry blossoms.'
    },
    'Paris': {
        'country': 'France',
        'population': 11276700,
        'fact': 'Home to the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")