# Resetting World — Hardware Architecture (`rw-hardware`)

> **Pillar 03 of Resetting World**: Open blueprints, power management, and hardware kits for sovereign, off-grid nodes.

[![License: CERN-OHL-P v2](https://img.shields.io/badge/Hardware%20License-CERN--OHL--P-green.svg)](https://ohwr.org/cern_ohl_p_v2.txt)
[![Target: Low Power](https://img.shields.io/badge/Power-5W%20to%2025W-yellow.svg)]()
[![Form Factor: Portable / Rugged](https://img.shields.io/badge/Design-Solar%20Ready%20%7C%20Off--Grid-purple.svg)]()

---

## 🌍 Overview / Visió General / Visión General

**EN**: `rw-hardware` provides validated bills of materials (BOM), 3D-printable rugged enclosures, solar power budgeting schematics, and wiring guides to assemble sovereign compute nodes that can run indefinitely disconnected from the public electrical grid.

**CA**: `rw-hardware` proporciona llistes de materials verificats (BOM), esquemes de disseny 3D per a caixes resistents a la intempèrie, esquemes de càrrega solar i gestió energètica per muntar nodes autònoms capaços d'operar de forma indefinida sense connexió a la xarxa elèctrica.

**ES**: `rw-hardware` provee listas de componentes homologados (BOM), carcasas 3D reforzadas, esquemas de alimentación solar con baterías LiFePO4 y diagramas de conexionado para desplegar nodos informáticos autosuficientes que operan independientemente de la red eléctrica comercial.

---

## 🛠️ Reference Hardware Profiles / Perfils de Referència

### 1. The Survival Beacon (Raspberry Pi 5 / RK3588)
* **Processor**: Broadcom BCM2712 Quad-core ARM Cortex-A76 @ 2.4GHz (or Orange Pi 5 Plus RK3588).
* **RAM**: 8GB LPDDR4X (Shared system + model memory).
* **Storage**: 256GB - 1TB High-Endurance NVMe SSD via PCIe HAT.
* **Radio**: SX1262 LoRa Transceiver HAT (868MHz EU / 915MHz US) + Wi-Fi 802.11ac AP.
* **Power Draw**: 4.5W (idle) / 12W (full vector search & model inference).
* **Power Supply**: 50W Monocrystalline Solar Panel + 12V 100Wh LiFePO4 battery pack + MPPT regulator.

### 2. Tactical Pocket Node (Mobile / Termux)
* **Hardware**: Any modern Android smartphone or tablet with 6GB+ RAM.
* **Power**: Internal 5000mAh battery + 15W portable folding USB solar charger.
* **Connectivity**: Wi-Fi Direct, Bluetooth Mesh, USB-OTG connection to Meshtastic LoRa node.

### 3. Community Central Hub (Rugged Mini-PC / Laptop)
* **Hardware**: AMD Ryzen 7 / Intel Core Ultra mini-PC or reconditioned laptop with 16GB-32GB RAM.
* **Storage**: 2TB NVMe SSD containing the full 50-capsule library and multi-language models.
* **Power**: 100W Solar + 500Wh portable power station (Jackery, EcoFlow or DIY 12V pack).

---

## 📐 Mechanical & Enclosure
* **STL Files**: 3D printable IP65 ruggedized weather-resistant casing for Raspberry Pi 5 with passive cooling heatsink.
* **Thermal Management**: Fanless aluminum conduction chassis to avoid moving mechanical parts in dusty disaster environments.

---

## 📚 Documentation & Governance

- **Verified Pi 5 BOM & Power Budget**: [`docs/BOM_RASPBERRY_PI_5.md`](./docs/BOM_RASPBERRY_PI_5.md)
- **For AI Agents**: [`AGENTS.md`](./AGENTS.md)
- **Contributing**: [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- **Code of Conduct**: [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)
- **Security & Electrical Safety**: [`SECURITY.md`](./SECURITY.md)
- **License**: [`LICENSE`](./LICENSE) (CERN-OHL-P v2)
