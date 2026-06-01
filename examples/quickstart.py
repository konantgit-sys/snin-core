#!/usr/bin/env python3
"""Quickstart: SNIN V5 Mesh Fabric — базовые компоненты."""
import asyncio
from snin import (
    SmartRouter,
    InMemoryCircuitBreaker,
    DHTNode,
    TTLCache,
)


def demo_circuit_breaker():
    """Circuit Breaker: 3 инцидента → блокировка канала."""
    print("=== Circuit Breaker Demo ===")
    cb = InMemoryCircuitBreaker()

    # Здоровый канал
    print(f"healthy_channel blocked? {cb.is_blocked('tcp')}")  # False

    # 3 быстрых инцидента
    for i in range(3):
        blocked = cb.record_incident("tcp")
        print(f"  incident {i+1}: circuit {'🔴 BLOCKED' if blocked else '🟢 ok'}")

    print(f"После 3 инцидентов: blocked? {cb.is_blocked('tcp')}")  # True
    cb.force_recovery("tcp")
    print(f"После force_recovery: blocked? {cb.is_blocked('tcp')}")  # False
    print()


def demo_dht():
    """DHT Node: регистрация и поиск агентов (async)."""
    print("=== DHT Node Demo ===")
    dht = DHTNode(port=0, bootstrap=())
    assert dht.is_running() == False
    print(f"✅ DHTNode создана (не запущена)")
    print()


def demo_ttl_cache():
    """TTL Cache: временное хранение с автоочисткой."""
    print("=== TTL Cache Demo ===")
    cache = TTLCache(maxsize=100, ttl=2)

    cache.add("event_1")
    print(f"event_1 in cache? {'event_1' in cache}")  # True

    import time
    time.sleep(3)
    print(f"event_1 in cache (after 3s)? {'event_1' in cache}")  # False (expired)
    print()


def demo_smart_router():
    """SmartRouter: создание и метрики."""
    print("=== SmartRouter Demo ===")
    router = SmartRouter()
    print(f"✅ Router created. Start time: {router.stats['start_time']}")
    print(f"   Stats keys: {len(router.stats)}")
    print()


async def main():
    print(f"{'='*50}")
    print(f"SNIN v{__import__('snin').__version__} — Quickstart")
    print(f"{'='*50}\n")

    demo_circuit_breaker()
    demo_dht()
    demo_ttl_cache()
    demo_smart_router()

    print(f"{'='*50}")
    print("✅ All demos passed! Install: pip install snin")
    print(f"{'='*50}")


if __name__ == "__main__":
    asyncio.run(main())
