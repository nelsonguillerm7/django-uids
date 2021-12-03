from datetime import date
import requests

from django.conf import settings


class BMXService:
    """Class created to consume BMX service"""

    BMX_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series"
    BMX_TOKEN = settings.BMX_TOKEN
    SERIES = ["SP68257", "SF43718"]

    @classmethod
    def headers(cls):
        """Method get headers"""
        headers = {"Bmx-Token": cls.BMX_TOKEN, "Content-Type": "application/json"}
        return headers

    @classmethod
    def get(cls, url):
        """Method get"""
        return requests.get(url=url, headers=cls.headers())

    @classmethod
    def get_series_values(cls, initial_date: date, final_date: date):
        """Method created build url for initial date and final date"""
        series = ",".join(list(cls.SERIES))
        url = f"%s/%s/datos/%s/%s/" % (cls.BMX_URL, series, initial_date, final_date)
        response = cls.get(url=url)
        return response
