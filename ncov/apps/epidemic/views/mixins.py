from datetime import datetime


class ProcessDateMixin(object):
    def process_date(self, **kwargs):
        dt_string = kwargs.get("date")
        dt = datetime.strptime(dt_string, "%Y%m%d")
        return dt
