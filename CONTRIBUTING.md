# Contributing to `rw-hardware`

`rw-hardware` builds validated, reproducible off-grid compute and radio nodes under **CERN-OHL-P v2**.

## Ways to Contribute

1. **Bill of Materials (BOM) Verification**:
   - Submit reproducible BOMs with power draw measurements (idle, inference peak, radio TX peak in Watts).
   - Prioritize widely available, repairable parts (Raspberry Pi 5, Orange Pi 5 / RK3588, NVMe PCIe HATs, SX1262 LoRa modules, 12V LiFePO4 batteries, MPPT charge controllers).
2. **3D Enclosures & Thermal Design**:
   - Provide OpenSCAD sources alongside `.stl`/`.step` exports for IP65 weather-resistant, passively cooled housings.
   - Verify printability without exotic supports on standard FDM printers (PETG/ASA recommended for UV/outdoor durability).
3. **Safety Mandates (Mandatory for PR Approval)**:
   - Every electrical schematic must specify **wire gauge**, **inline fuse ratings**, **reverse-polarity protection**, and **LiFePO4 BMS low-temp/over-current cutoffs**.
   - Never recommend unsafe lithium-ion (NMC/LCO) DIY packs without certified BMS protection.
