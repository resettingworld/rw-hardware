# AGENTS.md — `rw-hardware`

Instructions for AI coding and hardware-documentation agents working in **`resettingworld/rw-hardware`** (Pillar 03: Open Hardware Blueprints, Solar Power & Off-Grid Nodes).

---

## 1. Repository Purpose
`rw-hardware` maintains reproducible Bills of Materials (BOMs), power consumption profiles, wiring schematics, and 3D-printable enclosures (under **CERN-OHL-P v2**) for deploying Resetting World nodes without mains electricity.

---

## 2. Safety & Engineering Invariants
1. **Mandatory Electrical Protections**: Every battery/solar wiring document MUST specify:
   - Battery chemistry (prefer **LiFePO4** 12.8V for thermal safety and cycle life).
   - Dedicated BMS with over-charge, over-discharge, short-circuit, and low-temperature cutoffs.
   - Inline fuse ratings sized to wire gauge (AWG / mm^2).
   - MPPT charge controller voltage/current limits.
2. **Verified Power Budgets**: All hardware profiles must distinguish between **Idle (W)**, **Inference/Search Peak (W)**, and **LoRa TX Peak (W)** and compute realistic solar autonomy days.
3. **Passive Cooling Priority**: Enclosures for dusty/humid disaster environments (IP65 target) should favor passive aluminum heatsink conduction over failure-prone moving fans unless high-TDP mini-PCs require active airflow.
4. **No Proprietary Lock-In**: Prefer standard connectors (XT60, Anderson Powerpole, USB-C PD, PCIe M.2 NVMe, SMA antenna connectors) and commercial off-the-shelf components.

---

## 3. Documentation & CAD Standards
- Always include parametric source files (e.g., OpenSCAD `.scad`, KiCad `.kicad_sch`) alongside exported `.stl`, `.step`, or PDF schematics when submitting hardware designs.
- Provide clear print settings (material: PETG or ASA for outdoor UV resistance; infill; tolerances) for 3D-printed parts.
- Keep `docs/BOM_*.md` tables structured with Part, Spec, Qty, Power Draw, and Notes columns.
