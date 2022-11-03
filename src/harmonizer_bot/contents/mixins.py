from __future__ import annotations


class ScheduleBuildableMixin:
    def build_schedule(self, *, window: int | None = None):
        on_and_after_schedules = self.SCHEDULES.select_on_and_after(self._date)
        if window:
            on_and_after_schedules = on_and_after_schedules[:window]
        slot_to_dates_schedules = on_and_after_schedules.inverse()
        return [str(schedule) for schedule in slot_to_dates_schedules]
