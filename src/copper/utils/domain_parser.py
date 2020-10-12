import tldextract

from .helper_spiders import get_spiders_preffix


def get_domain_name(url: str) -> str:
    extracted_result = tldextract.extract(url)

    if extracted_result.subdomain and not extracted_result.subdomain == "www":
        return f"{extracted_result.subdomain}_{extracted_result.domain}"
    else:
        return extracted_result.domain


def is_available_domain(url: str, alert) -> bool:
    spiders = get_spiders_preffix()
    url_domain = get_domain_name(url)

    if url_domain in spiders:
        return True
    else:
        alert.error("Store not available!")
        alert.info(
            "Please open an issue requesting the inclusion of it: https://github.com/Leonardofreua/copper/issues/new"
        )
        return False
