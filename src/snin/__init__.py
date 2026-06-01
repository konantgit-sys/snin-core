"""
SNIN — Sovereign Network Intelligence Node.

Многоуровневая P2P mesh-сеть для AI-агентов с self-learning routing,
квантово-устойчивой криптографией и децентрализованным DHT.

Основные компоненты:
  - SmartRouter: multi-channel routing с self-learning через circuit breaker
  - NostrBridge: интеграция с Nostr (101+ relay)
  - DHTNode: распределённый реестр агентов (Kademlia + Redis)
  - ContentRouter: дедупликация и маршрутизация контента
  - EncryptionLayer: L2 шифрование mesh-пакетов
  - CircuitBreaker: failure isolation и graceful degradation
  - ExternalGateway: входная точка внешней сети
"""

__version__ = "5.0.0.dev1"
__author__ = "SNIN Network"
__license__ = "MIT"
