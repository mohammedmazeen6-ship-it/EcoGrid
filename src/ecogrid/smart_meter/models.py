from dataclasses import dataclass

@dataclass
class MeterReading:
    meter_id: str
    generation_kwh: float
    consumption_kwh: float
    timestamp: float

    @property
    def excess_energy(self) -> float:
        return max(0.0, self.generation_kwh - self.consumption_kwh)
