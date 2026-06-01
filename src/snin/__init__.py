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

from snin.smart_router import SmartRouter, InMemoryCircuitBreaker
from snin.nostr_bridge import NostrBridge
from snin.dht_node import DHTNode
from snin.circuit_breaker import CircuitBreakerManager, CircuitState, Channel
from snin.gossip_stream import GossipStream
from snin.graceful_degradation import GracefulDegradation
from snin.route_engine import RouteEngine
from snin.external_gateway import TCPGateway
from snin.reputation import get_reputation_for_pubkey
from snin.ttl_cache import TTLCache
from snin.mesh_crypto import (
    encrypt_for_agent, decrypt_from_agent, load_identity
)
from snin.content_router_v2 import (
    BloomFilter, FastDedup
)

__all__ = [
    "SmartRouter",
    "InMemoryCircuitBreaker",
    "NostrBridge",
    "DHTNode",
    "CircuitBreakerManager",
    "CircuitState",
    "Channel",
    "GossipStream",
    "GracefulDegradation",
    "RouteEngine",
    "TCPGateway",
    "BloomFilter",
    "FastDedup",
    "encrypt_for_agent",
    "decrypt_from_agent",
    "load_identity",
    "get_reputation_for_pubkey",
    "TTLCache",
]
