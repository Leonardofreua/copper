from typing import List

from scrapy import spiderloader
from scrapy.utils import project


def get_spiders() -> List[str]:
    settings = project.get_project_settings()
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    spiders = spider_loader.list()

    return spiders


def get_spiders_preffix() -> List[str]:
    spiders_preffix = []
    spiders = get_spiders()

    for spider in spiders:
        preffix = spider.split("_spider")[0]
        spiders_preffix.append(preffix)

    return spiders_preffix
