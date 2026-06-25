from datetime import datetime


class TimeModel:
    """Model sumber waktu aplikasi."""

    def now(self):
        return datetime.now()

    def today_iso(self, current_time=None):
        current_time = current_time or self.now()
        return current_time.date().isoformat()

    def time_iso(self, current_time=None):
        current_time = current_time or self.now()
        return current_time.time().replace(microsecond=0).isoformat()

    def display_datetime(self, current_time=None):
        current_time = current_time or self.now()
        return current_time.strftime("%d-%m-%Y %H:%M:%S")
