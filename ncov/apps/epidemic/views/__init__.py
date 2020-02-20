from datetime import datetime

import pygal
from django.views import generic
from pygal import Config as PygalConfig
from pygal.style import LightSolarizedStyle

from apps.epidemic.models import Epidemic

config = PygalConfig()
config.human_readable = True
config.style = LightSolarizedStyle


class EpidemicChartView(generic.ListView):
    model = Epidemic

    def _process_date(self):
        dt_string = self.kwargs.get("date")
        dt = datetime.strptime(dt_string, "%Y%m%d")
        return dt

    def get_queryset(self):
        qs = Epidemic.objects.filter(published_at=self._process_date())
        return qs

    def render_to_response(self, context, **response_kwargs):
        dt_str = self._process_date().strftime("%m月%d")
        treemap = pygal.Treemap(config)
        treemap.title = f"{dt_str} novel corona virus".upper()
        for row in context["object_list"]:
            treemap.add(
                row.province,
                [
                    {"value": row.cumulative_diagnosis, "label": "累计确诊"},
                    {"value": row.cumulative_suspect, "label": "累计疑似"},
                    {"value": row.cumulative_death, "label": "累计死亡"}
                ],
            )
        return treemap.render_django_response(**response_kwargs)
