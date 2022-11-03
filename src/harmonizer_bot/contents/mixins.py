class ScheduleBuildableMixin:
    def build_schedule(self):
        on_and_after_schedules = self.SCHEDULES.select_on_and_after(self._date)
        slot_to_dates_schedules = on_and_after_schedules.inverse(self._date)
        return [str(schedule) for schedule in slot_to_dates_schedules]
