import tldextract

from .spiders_handler import SpidersHandler


def get_domain_name(url: str) -> str:
    extracted_result = tldextract.extract(url)

    if extracted_result.subdomain and not extracted_result.subdomain == "www":
        return f"{extracted_result.subdomain}_{extracted_result.domain}"
    else:
        return extracted_result.domain


def validate_available_domain(url):  # type (str) -> Union[Any, Any]:
    spiders_list = SpidersHandler.get_spiders_list()
    spider_classes = SpidersHandler.get_spiders_classes(spiders_list)
    url_domain = get_domain_name(url)

    for spider in spider_classes:
        if url_domain == spider.name.split("_spider")[0]:
            return url_domain, spider
    else:
        return None, None
