import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from solar_budget import compute_solar_budget


def test_pi5_survival_beacon_budget():
    res = compute_solar_budget(
        idle_watts=4.8,
        peak_watts=12.5,
        peak_hours_per_day=2.5,
        battery_voltage_v=12.8,
        battery_ah=10.0,
        solar_panel_watts=50.0,
        peak_sun_hours=3.5,
    )
    assert res.daily_consumption_wh > 120
    assert res.solar_daily_harvest_wh > res.daily_consumption_wh
    assert res.autonomy_days_no_sun >= 0.8
    assert res.recommended_fuse_amps in [3, 5, 10, 15, 20, 30]
