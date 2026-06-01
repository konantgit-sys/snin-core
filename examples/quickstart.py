#!/usr/bin/env python3
"""Quickstart: запустить SNIN mesh-ноду и подключить агента."""
import asyncio
import os
import sys

# Добавляем src в путь (для запуска без установки)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from snin.smart_router import SmartRouter
from snin.external_gateway import AgentGateway


async def main():
    # 1. Создаём роутер
    router = SmartRouter(
        listen_host="127.0.0.1",
        listen_port=9932,
        health_port=9933,
        dht_port=9934,
        relay_list=["wss://relay.snin.network"],
    )

    # 2. Запускаем
    print("Starting SNIN Router...")
    router_task = asyncio.create_task(router.run())
    await asyncio.sleep(2)

    # 3. Проверяем статус
    print(f"Nostr shards: {len([w for w in router._nostr_writers if w])}/5")
    print("")

    # 4. Подключаем агента (пример)
    agent_nsec = os.environ.get("SNIN_NSEC", "nsec1...")
    gateway = AgentGateway(
        router_host="127.0.0.1",
        router_port=9932,
        agent_name="quickstart-agent",
        agent_nsec=agent_nsec,
    )
    await gateway.connect()
    print(f"Agent connected: {gateway.agent_name}")

    # 5. Отправляем сообщение
    await gateway.send({
        "kind": "message",
        "content": "Hello from SNIN Quickstart!",
    })
    print("Message sent!")

    # Даём поработать
    await asyncio.sleep(5)

    # Статистика
    stats = router.get_stats()
    print(f"\nStats: received={stats.get('received',0)} forwarded={stats.get('forwarded',0)}")


if __name__ == "__main__":
    asyncio.run(main())
