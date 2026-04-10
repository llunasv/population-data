import pytest
from population_analyzer import calculate_population_change

@pytest.fixture
def sample_data():
    return [
        {"country": "Ukraine", "year": 2020, "population": 12000000},
        {"country": "Ukraine", "year": 2021, "population": 10000000},
    ]

def test_calculate_change_structure(sample_data):
    results = calculate_population_change(sample_data)
    assert isinstance(results, dict)
    assert "Ukraine" in results

@pytest.mark.parametrize("country, y1, p1, y2, p2, expected", [
    ("Poland", 2020, 380, 2021, 381, 1),
    ("France", 2010, 65, 2011, 64, -1),
    ("Germany", 2022, 80, 2023, 80, 0),
])
def test_calculation_logic(country, y1, p1, y2, p2, expected):
    data = [
        {"country": country, "year": y1, "population": p1},
        {"country": country, "year": y2, "population": p2}
    ]
    res = calculate_population_change(data)
    year_range = f"{y1}-{y2}"
    assert res[country][0][year_range] == expected