from har2locust.plugin import entriesprocessor_with_args
from urllib.parse import urlsplit


@entriesprocessor_with_args  # use with-args version because it is executed last
def process(entries: list[dict], _args):
    # calculate headers shared by all requests (same name and value)
    default_headers = None
    for e in entries:
        headers = e["request"]["headers"]
        if default_headers is None:
            default_headers = headers[:]
        else:
            for dh in default_headers[:]:
                for h in headers:
                    if dh["name"] == h["name"]:
                        if dh["value"] != h["value"]:
                            default_headers.remove(dh)  # header has different value
                            break
                        break
                else:
                    default_headers.remove(dh)  # header not present
    if default_headers is None:
        default_headers = []

    default_headers.sort(key=lambda item: item["name"])

    urlparts = urlsplit(entries[0]["request"]["url"])
    host = f"{urlparts.scheme}://{urlparts.netloc}/"
    for e in entries:
        e["request"]["url"] = e["request"]["url"].removeprefix(host)
        headers = e["request"]["headers"]
        for h in headers[:]:
            for dh in default_headers:
                if h["name"] == dh["name"]:
                    headers.remove(dh)
        headers[:] = sorted(headers, key=lambda item: item["name"])

    return {"host": host, "default_headers": default_headers}
