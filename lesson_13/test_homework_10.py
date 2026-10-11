import logging

# Імпорт функції з файлу homework_10
from homework_10 import log_event

def test_log_event_success(caplog):
  # Перевіряємо статус 'success' (рівень INFO)
  with caplog.at_level(logging.INFO):
    log_event("Mariana", "success")

  # Перевіряємо, чи з'явився правильний текст у логах
  assert "Login event - Username: Mariana, Status: success" in caplog.text

def test_log_event_expired(caplog):
  # Перевіряємо статус 'expired' (рівень WARNING)
  with caplog.at_level(logging.WARNING):
    log_event("Mariana", "expired")

  assert "Login event - Username: Mariana, Status: expired" in caplog.text

def test_log_event_failed(caplog):
  # Перевіряємо статус 'failed' (рівень ERROR)
  with caplog.at_level(logging.ERROR):
    log_event("Mariana", "failed")

  assert "Login event - Username: Mariana, Status: failed" in caplog.text