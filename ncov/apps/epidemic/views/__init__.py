import pygal
from django.views import generic
from pygal import Config as PygalConfig
from pygal.style import LightSolarizedStyle

from apps.epidemic.models import Epidemic
from apps.epidemic.serializers import EpidemicTotalSerializer
from apps.epidemic.views.mixins import ProcessDateMixin

config = PygalConfig()
config.human_readable = True
config.style = LightSolarizedStyle


class EpidemicChartView(generic.ListView):
    model = Epidemic
    queryset = Epidemic.objects.total_group_by_date()

    def get_chart_data(self) -> dict:
        qs = self.get_queryset()
        cumulative_suspect = list(map(lambda x: x["cumulative_suspect__sum"], qs))
        cumulative_diagnosis = list(map(lambda x: x["cumulative_diagnosis__sum"], qs))
        cumulative_death = list(map(lambda x: x["cumulative_death__sum"], qs))
        return {
            "累计疑似": cumulative_suspect,
            "累计确诊": cumulative_diagnosis,
            "累计死亡": cumulative_death,
        }

    def get_chart_config(self):
        _config = config.copy()
        _config.x_label_rotation = 30
        _config.interpolate = "hermite"
        return _config

    def render_to_response(self, context, **response_kwargs):
        qs = self.get_queryset()

        line = pygal.Line(self.get_chart_config())
        line.title = f"novel corona virus".upper()
        # line.x_labels = list(map(lambda x: x["published_at"], qs))
        line.x_labels = map(lambda x: x["published_at"].strftime("%m-%d"), qs)
        for k, v in self.get_chart_data().items():
            line.add(k, v)
        return line.render_django_response(**response_kwargs)


class EpidemicDateChartView(ProcessDateMixin, generic.ListView):
    model = Epidemic

    def get_queryset(self):
        qs = Epidemic.objects.filter(published_at=self.process_date(**self.kwargs))
        return qs

    def render_to_response(self, context, **response_kwargs):
        dt_str = self.process_date(**self.kwargs).strftime("%m月%d")
        treemap = pygal.Treemap(config)
        treemap.title = f"{dt_str} novel corona virus".upper()
        for row in context["object_list"]:
            treemap.add(
                row.province,
                [
                    {"value": row.cumulative_diagnosis, "label": "累计确诊"},
                    {"value": row.cumulative_suspect, "label": "累计疑似"},
                    {"value": row.cumulative_death, "label": "累计死亡"},
                ],
            )
        return treemap.render_django_response(**response_kwargs)


class EpidemicDateTotalChartView(ProcessDateMixin, generic.DetailView):
    model = Epidemic

    def get_object(self, queryset=None):
        _obj = Epidemic.objects.total_by_date(self.process_date(**self.kwargs))
        ser = EpidemicTotalSerializer(_obj)
        return ser.data

    def render_to_response(self, context, **response_kwargs):
        dt_str = self.process_date(**self.kwargs).strftime("%m月%d")
        pie_chart = pygal.Pie(config)
        pie_chart.title = f"{dt_str} total novel corona virus".upper()
        for k, v in self.get_object().items():
            pie_chart.add(k.upper(), v)
        return pie_chart.render_django_response(**response_kwargs)
