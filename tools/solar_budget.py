"""Solar & LiFePO4 battery sizing calculator for Resetting World off-grid nodes."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PowerBudgetResult:
    """Computed energy balance and autonomy metrics."""

    daily_consumption_wh: float
    solar_daily_harvest_wh: float
    net_daily_surplus_wh: float
    autonomy_days_no_sun: float
    recommended_fuse_amps: int


def compute_solar_budget(
    idle_watts: float,
    peak_watts: float,
    peak_hours_per_day: float,
    battery_voltage_v: float,
    battery_ah: float,
    solar_panel_watts: float,
    peak_sun_hours: float = 3.5,
    dod_limit: float = 0.85,
    system_efficiency: float = 0.80,
) -> PowerBudgetResult:
    """Compute daily energy balance, no-sun autonomy days, and DC fuse sizing."""
    if idle_watts < 0 or peak_watts < idle_watts:
        raise ValueError("peak_watts must be >= idle_watts >= 0")
    if not (0 <= peak_hours_per_day <= 24):
        raise ValueError("peak_hours_per_day must be between 0 and 24")

    idle_hours = 24.0 - peak_hours_per_day
    daily_wh = (idle_watts * idle_hours) + (peak_watts * peak_hours_per_day)
    harvest_wh = solar_panel_watts * peak_sun_hours * system_efficiency

    usable_battery_wh = battery_voltage_v * battery_ah * dod_limit
    autonomy_days = usable_battery_wh / daily_wh if daily_wh > 0 else 0.0

    # Size inline fuse at ~150% of peak current rounded up to standard blade fuse step
    peak_amps = (peak_watts / battery_voltage_v) * 1.5
    standard_fuses = [3, 5, 10, 15, 20, 30]
    fuse_amps = next((f for f in standard_fuses if f >= peak_amps), 30)

    return PowerBudgetResult(
        daily_consumption_wh=round(daily_wh, 2),
        solar_daily_harvest_wh=round(harvest_wh, 2),
        net_daily_surplus_wh=round(harvest_wh - daily_wh, 2),
        autonomy_days_no_sun=round(autonomy_days, 2),
        recommended_fuse_amps=fuse_amps,
    )
