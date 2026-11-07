import pytest


def test_pytest_is_working():
    """Базовый тест для проверки успешного прохождения CI."""
    assert True


@pytest.mark.django_db
def test_django_db_connection():
    """Проверка того, что тестовая БД успешно создается и доступна."""
    assert True
