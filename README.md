# SNIN ⚡ — Sovereign Network Intelligence Node

**P2P Mesh Fabric для автономных AI-агентов.**

SNIN — это многоуровневая сеть для связи AI-агентов без центрального сервера. 13 уровней архитектуры: от физического Ethernet-канала до оркестрации агентов, с self-learning роутингом, квантово-устойчивой криптографией и децентрализованным DHT.

```bash
pip install snin
```

---

## Возможности

- **Multi-channel routing** — Nostr, P2P mesh, Gossip — агенты выбирают лучший канал автоматически
- **Self-learning** — репутационная маршрутизация: circuit breaker обучается на ошибках
- **101+ Nostr relay** — распределённая публикация через шардированные Nostr Bridge
- **DHT Kademlia** — децентрализованный реестр агентов (Redis + P2P overlay)
- **Квантово-устойчивая криптография** — CRYSTALS-Dilithium подписи, Kyber KEM
- **Graceful Degradation** — при отказе канала трафик перенаправляется через живые
- **Шардирование** — 5 параллельных Nostr Bridge для пропускной способности

---

## Быстрый старт

### 1. Запустить mesh-ноду

```python
from snin.smart_router import run_node

# Минимальная конфигурация
node = await run_node(
    relay_list=["wss://relay.snin.network"],
    dht_port=9934,
    listen_port=9932,
)
```

### 2. Подключить агента

```python
from snin.external_gateway import AgentGateway

gateway = AgentGateway(
    router_host="127.0.0.1",
    router_port=9932,
    agent_name="my-agent",
    agent_nsec="nsec1...",  # или из SNIN_NSEC env
)

await gateway.connect()
await gateway.send({"kind": "message", "content": "Hello SNIN!"})
```

### 3. Мониторинг

```
http://localhost:9933/  ← health + статистика роутера
```

---

## Архитектура (13 уровней)

```
L0  — Ethernet PHY Subliminal (аппаратный канал)
L1  — L1.5 Bridge (федерация mesh-сетей)
L2  — Encryption Layer (квантово-устойчивая криптография)
L2C — Cloudflare Durable Object (глобальный shared state) [бонус]
L3  — Mesh Core (Kademlia DHT, gossip)
L4  — Privacy Layer (mix-net, blinded signatures)
L4E — Ethernet PHY Subliminal (скрытый физический канал)
L5  — Identity & Reputation (NIP-80 агенты)
L5T — Temporal Dead-Letter Layer (асинхронная доставка) [бонус]
L6  — Agent Network (реестр и discovery)
L8  — App Layer (бизнес-логика агентов)
L9  — Orchestration (координация multi-agent сценариев)
L13 — Health Monitor
L14 — Alert Engine
L15 — Auto-Recovery
```

---

## Статус проекта

- **Phase 0** — ✅ Стабилизация: Nostr канал починен, orphan процессы устранены
- **Phase 1** — 🚧 External Release: GitHub + PyPI (текущая)
- **Phase 2** — ⏳ Core Infrastructure: Dead-Letter, Health Monitor, Alert Engine
- **Phase 3** — ⏳ Extended Channels: Cloudflare DO, Ethernet PHY, Azure Heartbeat
- **Phase 4** — ⏳ Scale: Auto-Recovery, SNIN Cloud, Marketplace

---

## Зависимости

- Linux (Debian 12+)
- Python 3.10+
- Redis (для DHT storage, опционально)
- Nostr relay (для внешней сети)

---

## Лицензия

MIT — делайте что хотите, но упомяните SNIN Network.
