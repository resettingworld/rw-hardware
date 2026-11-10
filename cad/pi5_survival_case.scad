// Resetting World - Raspberry Pi 5 + LoRa Survival Beacon Case
// Parametric OpenSCAD Chassis (CERN-OHL-P v2)
// Recommended material: PETG or ASA (outdoor UV & heat resistance), 40% gyroid infill

wall = 3.2;
inner_w = 94.0;
inner_d = 66.0;
inner_h = 34.0; // Clearance for M.2 NVMe HAT + passive armor heatsink

module rounded_box(w, d, h, r=4) {
    hull() {
        for (x=[r, w-r], y=[r, d-r]) {
            translate([x, y, 0]) cylinder(h=h, r=r, $fn=32);
        }
    }
}

difference() {
    rounded_box(inner_w + 2*wall, inner_d + 2*wall, inner_h + wall, r=5);
    translate([wall, wall, wall])
        rounded_box(inner_w, inner_d, inner_h + 1, r=3);
    // SMA LoRa antenna bulkhead hole (6.5mm)
    translate([-1, wall + 18, wall + 20])
        rotate([0, 90, 0]) cylinder(h=wall + 4, d=6.5, $fn=24);
    // USB-C PD 5V power grommet cutout
    translate([wall + 14, -1, wall + 6])
        cube([14, wall + 4, 9]);
}
