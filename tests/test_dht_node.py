"""Test dht_node — DHTNode асинхронные методы."""
import pytest
from snin.dht_node import DHTNode


class TestDHTNode:
    """DHTNode — распределённый реестр (async)."""

    @pytest.mark.asyncio
    async def test_create(self):
        node = DHTNode(port=0, bootstrap=())
        assert node is not None
        assert node.is_running() == False

    @pytest.mark.asyncio
    async def test_register_and_lookup(self):
        node = DHTNode(port=0, bootstrap=())
        await node.register_agent(
            "abc123pubkey",
            {"host": "127.0.0.1", "port": 9933, "name": "test_agent"}
        )
        info = await node.lookup_agent("abc123pubkey")
        assert info is not None

    @pytest.mark.asyncio
    async def test_lookup_missing_returns_none(self):
        node = DHTNode(port=0, bootstrap=())
        info = await node.lookup_agent("nonexistent_pubkey")
        assert info is None

    @pytest.mark.asyncio
    async def test_list_agents(self):
        node = DHTNode(port=0, bootstrap=())
        agents = await node.list_agents()
        assert isinstance(agents, list)
