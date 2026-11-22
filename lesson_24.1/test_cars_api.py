import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"  # Локальний сервер Flask для тестування

# Налаштовую логування і в консоль, і у файл test_search.log
logger = logging.getLogger("cars_api_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    log_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler("lesson_24.1/test_search.log", mode="w", encoding="utf-8")
    file_handler.setFormatter(log_format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


class TestCarsAPI:
    """Перевірка пошуку авто через GET /cars після входу в систему."""

    @pytest.fixture(scope="class")
    def auth_session(self):
        """
        Фікстура рівня класу: один раз авторизується через /auth,
        отримує access_token і додає його в заголовки сесії.
        """
        session = requests.Session()
        logger.info("Вхід через POST /auth для отримання токена...")

        response = session.post(
            f"{BASE_URL}/auth",
            auth=HTTPBasicAuth("test_user", "test_pass"),
            timeout=5,
        )
        assert response.status_code == 200, f"Не вдалося увійти: {response.status_code}"

        token = response.json().get("access_token")
        assert token, "У відповіді відсутній access_token"

        session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info("Авторизація пройшла успішно, токен збережено в сесії.")

        yield session
        session.close()

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 10),         # Сортування за ціною, ліміт 10
            ("price", 3),          # Сортування за ціною, ліміт 3
            ("year", 5),           # Сортування за роком, ліміт 5
            ("engine_volume", 2),  # Сортування за об'ємом двигуна, ліміт 2
            ("brand", 4),          # Сортування за маркою, ліміт 4
            ("price", 1),          # Сортування за ціною, ліміт 1
        ],
    )
    def test_get_cars(self, auth_session, sort_by, limit):
        """Перевіряю GET /cars з різними значеннями sort_by та limit."""
        params = {"sort_by": sort_by, "limit": limit}
        logger.info("Запит GET /cars з параметрами %s", params)

        response = auth_session.get(f"{BASE_URL}/cars", params=params, timeout=5)
        logger.info("Статус відповіді: %s", response.status_code)

        assert response.status_code == 200

        cars = response.json()
        logger.info("Отримано авто: %s (ліміт: %s)", len(cars), limit)

        assert isinstance(cars, list)
        assert len(cars) <= limit

        required_keys = {"brand", "year", "engine_volume", "price"}
        for car in cars:
            assert required_keys.issubset(car.keys())

        if len(cars) > 1 and sort_by in {"price", "year", "engine_volume"}:
            values = [car[sort_by] for car in cars]
            assert values == sorted(values) or values == sorted(values, reverse=True)


