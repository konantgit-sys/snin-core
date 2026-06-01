"""Test circuit_breaker — CircuitBreakerManager и Channel."""
import pytest
from snin.circuit_breaker import CircuitBreakerManager, get_circuit_breaker, Channel


class TestCircuitBreakerManager:
    """CircuitBreakerManager — управление каналами с CB."""

    def test_create(self):
        mgr = CircuitBreakerManager()
        assert mgr is not None
        mgr.setup_channels()
        assert len(mgr.get_healthy_channels()) > 0

    def test_get_status_returns_dict(self):
        mgr = CircuitBreakerManager()
        status = mgr.get_status()
        assert isinstance(status, dict)

    def test_singleton_via_get_circuit_breaker(self):
        cb = get_circuit_breaker()
        assert isinstance(cb, CircuitBreakerManager)


class TestChannel:
    """Channel — индивидуальный канал с CB."""

    def test_can_process_initially(self):
        ch = Channel(name="test")
        ok, msg = ch.can_process_request()
        assert ok == True
        assert msg is None

    def test_record_failure(self):
        ch = Channel(name="test")
        ch.record_failure("timeout")
        assert ch.failure_count == 1

    def test_record_success(self):
        ch = Channel(name="test")
        ch.record_success()
        assert ch.success_count == 1
        assert ch.request_count == 1

    def test_half_open_on_failure_threshold(self):
        ch = Channel(name="test")
        for _ in range(3):
            ch.record_failure("error")
        ok, msg = ch.can_process_request()
        assert ok == False
        assert "OPEN" in msg or "open" in msg

    def test_recovery_via_success(self):
        ch = Channel(name="test")
        for _ in range(3):
            ch.record_failure("error")
        # Теперь state должен быть OPEN
        # Принудительно HALF_OPEN
        from snin.circuit_breaker import CircuitState
        ch.state = CircuitState.HALF_OPEN
        # Успешный запрос → CLOSED
        ch.record_success()
        assert ch.state == CircuitState.CLOSED
        assert ch.failure_count == 0
