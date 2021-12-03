from datetime import date
import requests

from django.conf import settings


class BMXService:
    BMX_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series"
    BMX_TOKEN = settings.BMX_TOKEN
    SERIES = ["SP68257", "SF43718"]

    @classmethod
    def headers(cls):
        headers = {"Bmx-Token": cls.BMX_TOKEN, "Content-Type": "application/json"}
        return headers

    @classmethod
    def get(cls, url):
        return requests.get(url=url, headers=cls.headers())

    @classmethod
    def get_series_values(cls, initial_date: date, final_date: date):
        series = ",".join(list(cls.SERIES))
        url = f"%s/%s/datos/%s/%s/" % (cls.BMX_URL, series, initial_date, final_date)
        response = cls.get(url=url)
        return response
