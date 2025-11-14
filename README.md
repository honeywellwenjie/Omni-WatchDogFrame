# Omni-WatchDogFrame — A Cross-Platform Hybrid Watchdog Framework for Embedded Reliability

Omni-WatchDogFrame is a hybrid software-hardware watchdog framework designed to provide high-reliability process supervision across heterogeneous embedded platforms.
While most embedded systems expose only a single hardware watchdog device, Omni-WatchDogFrame virtualizes this mechanism and builds a multi-layer software watchdog infrastructure on top of it, enabling unlimited software-level watchdog instances for different modules, threads, or critical services.

Hybrid Two-Layer Watchdog Architecture

The framework operates by combining:

A hardware watchdog (HW-WDT)
– the final fail-safe mechanism, responsible for system-level recovery;

A software watchdog subsystem (SW-WDT)
– flexible, dynamic, and capable of supervising any number of software components.

The software layer continuously monitors active processes/threads and reports their status to the hardware watchdog.
If any critical software watchdog fails, times out, or its supervision thread dies, the framework intentionally stops kicking the hardware watchdog, allowing the hardware watchdog to perform a clean system reset.

This ensures strict “fail-safe by design” behavior.

![Architecture Diagram](docs/architecture.jpg)
