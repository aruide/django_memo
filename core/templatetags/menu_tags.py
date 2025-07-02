from django import template
from django.urls import get_resolver, reverse, NoReverseMatch, URLPattern, URLResolver
from collections import defaultdict

register = template.Library()

def _get_urls(patterns, prefix=''):
    urls_dict = defaultdict(list)

    for pattern in patterns:
        if isinstance(pattern, URLPattern):
            if pattern.name:
                full_name = prefix + pattern.name
                try:
                    url = reverse(full_name)
                    if pattern.name == "index" and prefix:  # lien principal du namespace
                        ns = prefix.rstrip(":")
                        urls_dict[ns].insert(0, {"name": ns, "url": url})
                    else:
                        ns = prefix.rstrip(":") if prefix else "root"
                        urls_dict[ns].append({"name": pattern.name, "url": url})
                except NoReverseMatch:
                    continue  # skip les routes avec arguments
        elif isinstance(pattern, URLResolver):
            new_prefix = prefix + pattern.namespace + ":" if pattern.namespace else prefix
            sub_urls = _get_urls(pattern.url_patterns, new_prefix)
            for ns, items in sub_urls.items():
                urls_dict[ns].extend(items)

    return urls_dict

@register.simple_tag
def get_all_named_urls():
    resolver = get_resolver()
    all_urls = _get_urls(resolver.url_patterns)
    # ne pas afficher les routes d'admin
    return {k: v for k, v in all_urls.items() if k != "admin"}
