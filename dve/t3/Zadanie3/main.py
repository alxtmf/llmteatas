class Country:
    def __init__(self, name, capital, population, area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
def sort_countries_by_density(countries):
    sorted_countries = sorted(countries, key=lambda x: x.population / x.area, reverse=True)
    return sorted_countries
def search_country_by_name(countries, name):
    for country in countries:
        if country.name.lower() == name.lower():
            return country
    return None
def edit_country(countries, index, new_name, new_capital, new_population, new_area):
    if 0 <= index < len(countries):
        country = countries[index]
        country.name = new_name
        country.capital = new_capital
        country.population = new_population
        country.area = new_area
        return True
    else:
        print("Неверный индекс")
        return False
def delete_country(countries, index):
    if 0 <= index < len(countries):
        del countries[index]
        return True
    else:
        print("Неверный индекс")
        return False
def print_countries(countries):
    print("{:<5} {:<20} {:<20} {:<20} {:<20}".format("№", "Название", "Столица", "Население", "Площадь"))
    for i, country in enumerate(countries):
        print("{:<5} {:<20} {:<20} {:<20} {:<20}".format(i+1, country.name, country.capital, country.population, country.area))
    print("Всего стран:", len(countries))
test_countries = [
    Country("Россия", "Москва", 144000000, 17098242),
    Country("Китай", "Пекин", 1400000000, 9596961),
    Country("США", "Вашингтон", 331000000, 9833517)
]
def run_unit_tests():
    try:
        sorted_countries = sort_countries_by_density(test_countries)
        assert sorted_countries[0].name == "Китай"
        found_country = search_country_by_name(test_countries, "Россия")
        assert found_country.capital == "Москва"
        edit_success = edit_country(test_countries, 1, "Китай", "Пекин", 1400000000, 9596961)
        assert edit_success is True
        assert test_countries[1].name == "Китай"
        delete_success = delete_country(test_countries, 0)
        assert delete_success is True
        assert len(test_countries) == 2
        print("Тесты пройдены успешно")
    except AssertionError:
        print("Не все тесты пройдены успешно")
if __name__ == "__main__":
    run_unit_tests()
    print("\n---\n")
    print_countries(test_countries)
