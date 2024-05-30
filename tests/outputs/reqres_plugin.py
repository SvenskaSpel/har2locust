from locust import events, run_single_user, task

import os
import re

from locust_plugins import listeners
from svs_locust import RestUser

os.environ["LOCUST_TEST_ENV"] = "test3"
os.environ["LOCUST_TENANT"] = "lb"


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    import time

    environment.events.request.add_listener(lambda *args, **kw: time.sleep(0.1))
    listeners.StopUserOnFail(environment)


class reqres_in(RestUser):
    default_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "sv,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    }

    @task
    def t(self):
        with self.rest("POST", "/api/register", json={"email": "eve.holt@reqres.in", "password": "pistol"}) as resp:
            job = re.findall('"token":"([^"]*)"', resp.text)[0] if resp.text else None
        with self.rest("PATCH", "/api/users/2", json={"name": "morpheus", "job": job}) as resp:
            pass


if __name__ == "__main__":
    run_single_user(reqres_in)
