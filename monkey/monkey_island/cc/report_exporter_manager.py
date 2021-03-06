import logging

__author__ = 'maor.rayzin'

logger = logging.getLogger(__name__)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ReportExporterManager(object):
    __metaclass__ = Singleton

    def __init__(self):
        self._exporters_set = set()

    def get_exporters_list(self):
        return self._exporters_set

    def add_exporter_to_list(self, exporter):
        self._exporters_set.add(exporter)

    def export(self, report):
        try:
            for exporter in self._exporters_set:
                exporter().handle_report(report)
        except Exception as e:
            logger.exception('Failed to export report')
