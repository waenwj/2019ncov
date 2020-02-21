import pendulum
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField


class Epidemic(models.Model):
    epidemics = JSONField()
    crawled_at = models.DateTimeField(
        _("crawled datetime"), db_index=True, editable=False, default=timezone.now
    )

    class Meta:
        ordering = ["-crawled_at"]


class TotalEpidemic(models.Model):
    epidemics = JSONField()
    crawled_at = models.DateTimeField(
        _("crawled datetime"), db_index=True, editable=False, default=timezone.now
    )

    class Meta:
        ordering = ["-crawled_at"]

    @property
    def title(self) -> str:
        _title = self.epidemics.get("totalConfirmAddCnt", 0)
        return f"国家卫健委：国内累计报告新型冠状病毒感染的肺炎确诊病例{_title}例"

    @property
    def totalHealAddCnt(self) -> int:
        _totalHealAddCnt = self.epidemics.get("totalHealAddCnt", 0)
        if not isinstance(_totalHealAddCnt, int):
            _totalHealAddCnt = int(_totalHealAddCnt)
        return _totalHealAddCnt

    @property
    def totalDeadAddCnt(self) -> int:
        _totalDeadAddCnt = self.epidemics.get("totalDeadAddCnt", 0)
        if not isinstance(_totalDeadAddCnt, int):
            _totalHealAddCnt = int(_totalDeadAddCnt)
        return _totalDeadAddCnt

    @property
    def totalSuspectedAddCnt(self) -> int:
        _totalSuspectedAddCnt = self.epidemics.get("totalSuspectedAddCnt", 0)
        if not isinstance(_totalSuspectedAddCnt, int):
            _totalSuspectedAddCnt = int(_totalSuspectedAddCnt)
        return _totalSuspectedAddCnt

    @property
    def totalNowConfirmCnt(self) -> int:
        _totalNowConfirmCnt = self.epidemics.get("totalConfirmAddCnt", 0)
        if not isinstance(_totalNowConfirmCnt, int):
            _totalNowConfirmCnt = int(_totalNowConfirmCnt)
        return _totalNowConfirmCnt

    @property
    def updateTime(self):
        _updateTime = self.epidemics.get("updateTime")
        dt = pendulum.from_format(_updateTime, "MM月DD日 HH时", tz="Asia/Shanghai")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
