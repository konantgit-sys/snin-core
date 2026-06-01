"""Test smart_router — базовая инициализация и API."""
import pytest
import os
import time

from snin.smart_router import SmartRouter, InMemoryCircuitBreaker


class TestSmartRouterInit:
    """SmartRouter создаётся без внешних зависимостей."""

    def test_create_default(self):
        """Создание с умолчаниями — не падает."""
        r = SmartRouter()
        assert isinstance(r, SmartRouter)
        assert r.stats["start_time"] > 0

    def test_stats_is_dict(self):
        """stats — словарь с метриками."""
        r = SmartRouter()
        assert isinstance(r.stats, dict)
        assert "start_time" in r.stats


class TestInMemoryCircuitBreaker:
    """InMemoryCircuitBreaker — sliding window CB из smart_router.py."""

    def test_create(self):
        cb = InMemoryCircuitBreaker()
        assert cb is not None
        assert cb.incident_limit == 3
        assert cb.incident_window == 60

    def test_channel_not_blocked_by_default(self):
        cb = InMemoryCircuitBreaker()
        assert cb.is_blocked("test_channel") == False

    def test_one_incident_not_enough_to_block(self):
        cb = InMemoryCircuitBreaker()
        blocked = cb.record_incident("test_channel")
        assert blocked == False
        assert cb.is_blocked("test_channel") == False

    def test_three_incidents_block_channel(self):
        cb = InMemoryCircuitBreaker()
        for _ in range(3):
            blocked = cb.record_incident("bad_channel")
        # После 3 инцидентов — True (заблокирован)
        assert blocked == True
        assert cb.is_blocked("bad_channel") == True

    def test_force_recovery_unblocks(self):
        cb = InMemoryCircuitBreaker()
        for _ in range(3):
            cb.record_incident("chan")
        assert cb.is_blocked("chan") == True
        cb.force_recovery("chan")
        assert cb.is_blocked("chan") == False

    def test_get_blocked_returns_only_blocked(self):
        cb = InMemoryCircuitBreaker()
        for _ in range(3):
            cb.record_incident("blocked_chan")
        blocked_list = cb.get_blocked()
        assert "blocked_chan" in blocked_list
        assert "good_chan" not in blocked_list

    def test_reset_clears_incidents_and_block(self):
        cb = InMemoryCircuitBreaker()
        for _ in range(3):
            cb.record_incident("chan")
        assert cb.is_blocked("chan") == True
        cb.reset("chan")
        assert cb.is_blocked("chan") == False
        # После reset — снова пропускаем
        blocked = cb.record_incident("chan")
        assert blocked == False
