# Hardware Profile 01: Survival Beacon (Raspberry Pi 5 + Solar LiFePO4)

- **Repository**: `resettingworld/rw-hardware`
- **License**: CERN-OHL-P v2

---

## 1. System Summary
Low-power (5W–15W), fanless off-grid compute & LoRa mesh relay capable of serving the full 50-capsule `rw-knowledge` library and `rw-protocol` node indefinitely on solar energy.

## 2. Verified Bill of Materials (BOM)

| Component | Recommended Specification | Qty | Typical Power | Notes |
|---|---|---|---|---|
| **Compute SBC** | Raspberry Pi 5 (8GB RAM) | 1 | 3.5W idle / 10W peak | 4GB minimum for Matryoshka `--dim 256` |
| **NVMe HAT + SSD** | PCIe M.2 HAT+ & 512GB NVMe (2230/2242) | 1 | 1.0W – 2.5W | Holds all 50 RAG capsules + local LLM weights |
| **Cooling** | Passive CNC Aluminum Armor Heatsink Case | 1 | 0W | Avoids dust/fan bearing failures |
| **LoRa Radio** | SX1262 LoRa Module (868MHz EU / 915MHz US) + 3dBi SMA Antenna | 1 | 0.1W RX / 0.6W TX | Connect via USB-C or UART GPIO |
| **Battery** | 12.8V 10Ah LiFePO4 (128Wh) with integrated 10A BMS | 1 | — | Must include low-temp (<0°C) charge cutoff |
| **Solar Panel** | 50W Monocrystalline 18V Vmp Foldable/Rigid | 1 | +50W peak input | Sized for overcast winter recharge |
| **Solar Controller** | 10A MPPT Solar Charge Controller (12V LiFePO4 profile) | 1 | 0.2W self-draw | Never wire solar directly to battery |
| **Buck Converter** | 12V to 5.1V 5A (25W+) USB-C PD DC-DC Converter | 1 | ~92% efficiency | Must sustain 5A rail for Pi 5 PCIe NVMe |
| **Protection** | Inline Blade Fuse Holder + 10A & 5A Automotive Fuses | 2 | — | Mandatory between battery, MPPT, and DC-DC |

## 3. Power & Autonomy Budget
- **Continuous Load (Idle + LoRa RX + Wi-Fi AP)**: ~4.8W
- **Peak Load (Active RAG Query / Local Inference)**: ~12.5W
- **24h Energy Consumption (average mixed emergency use)**: ~135 Wh/day
- **Battery Autonomy (no sun)**: ~24 hours continuous, or **3–4 days** with duty-cycled wake/query windows.

## 4. Mandatory Safety Warnings
- **NEVER operate LoRa transmitters without an antenna connected** to the SMA port (reflected RF power will destroy the SX1262 PA stage).
- **ALWAYS install an inline fuse within 15 cm of the LiFePO4 positive terminal** to prevent fire hazard in short-circuit events.
- **DO NOT charge LiFePO4 cells below 0°C (32°F)**; rely on a BMS with low-temperature cutoff.
