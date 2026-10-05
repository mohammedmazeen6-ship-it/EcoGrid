from .models import MeterReading

class SmartMeterService:
    def ingest(self, meter_id, generation_kwh, consumption_kwh, timestamp):
        if generation_kwh < 0 or consumption_kwh < 0:
            raise ValueError("Energy values cannot be negative")

        reading = MeterReading(
            meter_id=meter_id,
            generation_kwh=generation_kwh,
            consumption_kwh=consumption_kwh,
            timestamp=timestamp,
        )

        return {
            "type": "MeterReadingValidated",
            "meter_id": reading.meter_id,
            "generation_kwh": reading.generation_kwh,
            "consumption_kwh": reading.consumption_kwh,
            "excess_kwh": reading.excess_energy,
            "timestamp": reading.timestamp,
        }
