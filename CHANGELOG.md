# Changelog

## [5.0.0.dev1] — 2026-06-01

### Added
- Initial SNIN V5 Mesh Fabric open-source release.
- 12 core modules: SmartRouter, NostrBridge, DHTNode, CircuitBreaker, ContentRouter,
  ExternalGateway, GossipStream, EncryptionLayer, RouteEngine, CPUScaler, AntiDDoS, TTLCache.
- 4-channel delivery: direct (TCP), mesh (Content Router), gossip (broadcast), nostr (public relays).
- GracefulDegradation — self-managed fallback when channels fail.
- InMemoryCircuitBreaker — sliding-window failure detection (3 incidents → 30s block).
- Environment-based configuration (all `SNIN_*` env vars).
- Python 3.10+ support, zero external Redis dependency for basic operation.
- Batch build passes, 12/12 modules verified.

### Changed
- All hardcoded file paths replaced with `SNIN_*` environment variables.
- All `sys.path.insert` hacks removed — proper package imports.
- Encryption layer: configurable port/pidfile/identities via env vars.

### Fixed
- No hardcoded nsec keys in source tree.
- All internal imports use `from snin.xxx import` pattern.

### Security
- All sensitive paths configurable via environment.
- No secrets in code.
- MIT license.
