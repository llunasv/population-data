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