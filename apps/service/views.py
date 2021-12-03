# Create your views here.
import json
import statistics
from datetime import date, datetime

from django.views.generic import FormView

from apps.service.forms import RangeTimeForm
from apps.service.service import BMXService


class GraphView(FormView):
    form_class = RangeTimeForm
    template_name = "base/base.html"

    def unix_date(self, date_value):
        """Function convert date format unix"""
        date_value = datetime.strptime(date_value, "%d/%m/%Y")
        return int(datetime.timestamp(date_value)) * 1000

    def operations(self, values_list: dict):
        """Clean data and operations"""
        values = [float(key["dato"]) for key in values_list]
        graph = [
            [self.unix_date(key["fecha"]), float(key["dato"])] for key in values_list
        ]
        kwargs = {
            "max_value": max(iter(values)),
            "min_value": min(iter(values)),
            "mean_value": statistics.mean(values),
            "graph": json.dumps(graph),
        }
        return kwargs

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        context = super().get_context_data(**kwargs)
        if "initial_date" in kwargs and "final_date" in kwargs:
            response = BMXService.get_series_values(**kwargs)
            if response.status_code == 200:
                result = response.json()
                print(result)
                serie1 = result["bmx"]["series"][0]
                if "datos" in serie1:
                    serie1.update({**self.operations(serie1["datos"])})

                serie2 = result["bmx"]["series"][1]
                if "datos" in serie2:
                    serie2.update({**self.operations(serie2["datos"])})
                context.update({"serie1": serie1, "serie2": serie2})
        return context

    def form_valid(self, form):
        """Overriding the behavior of the form_valid"""
        kwargs = {**form.cleaned_data}
        return self.render_to_response(self.get_context_data(**kwargs))

    def get(self, request, *args, **kwargs):
        """Overriding the behavior of the get initial dates"""
        kwargs = {
            **kwargs,
            "initial_date": datetime.strptime("01/12/2018", "%d/%m/%Y").date(),
            "final_date": date.today(),
        }
        return self.render_to_response(self.get_context_data(**kwargs))
