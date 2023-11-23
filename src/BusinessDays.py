import datetime
import bizdays


class bussinessDays():
    def brazilian_calendar(self):
        """Create the holidays calendar from Anbima repository"""
        cal = bizdays.Calendar.load(name='ANBIMA')
        return cal

    def du_252(self, start_date: datetime.date, end_date: datetime.date, cal: bizdays.Calendar) -> float:
        return cal.bizdays(date_from=start_date, date_to=end_date)/252

    def du_next_day(self, day_to_adjust: datetime.date, cal: bizdays.Calendar) -> float:
        return cal.adjust_next(dt=day_to_adjust)