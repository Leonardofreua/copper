from typing import List

from scrapy import spiderloader
from scrapy.utils import project


class SpidersHandler:
    __settings = project.get_project_settings()
    __spider_loader = spiderloader.SpiderLoader.from_settings(__settings)

    @classmethod
    def get_spiders_list(cls) -> List[str]:
        spiders = cls.__spider_loader.list()
        return spiders

    @classmethod
    def get_spiders_classes(cls, spiders_list: List[str]):
        spider_classes = [cls.__spider_loader.load(name) for name in spiders_list]
        return spider_classes
