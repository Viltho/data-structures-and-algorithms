import pytest

from CodeChallenge28.comparisons import sort_by_title, sort_by_year

movies = [
    {"title": "The Dark Knight", "year": 2008},
    {"title": "Pulp Fiction", "year": 1994},
    {"title": "Inception", "year": 2010},
    {"title": "The Shawshank Redemption", "year": 1994},
    {"title": "The Godfather", "year": 1972},
]

# Test for sort_by_year function
def test_sort_by_year():
    sorted_movies = sort_by_year(movies)
    expected_result = [
        {"title": "Inception", "year": 2010},
        {"title": "The Dark Knight", "year": 2008},
        {"title": "Pulp Fiction", "year": 1994},
        {"title": "The Shawshank Redemption", "year": 1994},
        {"title": "The Godfather", "year": 1972},
    ]
    assert sorted_movies == expected_result
    print("sort_by_year test passed")

# Test for sort_by_title function
def test_sort_by_title():
    sorted_movies = sort_by_title(movies)
    expected_result = [
    {"title": "The Dark Knight", "year": 2008},
    {"title": "The Godfather", "year": 1972},
    {"title": "Inception", "year": 2010},
    {"title": "Pulp Fiction", "year": 1994},
    {"title": "The Shawshank Redemption", "year": 1994},
    ]
    assert sorted_movies == expected_result
    print("sort_by_title test passed")
