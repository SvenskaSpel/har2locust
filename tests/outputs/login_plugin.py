from locust import events, run_single_user, task

import os

from locust_plugins.listeners import StopUserOnFail
from svs_locust import RestUser

os.environ["LOCUST_TEST_ENV"] = "itp1"
os.environ["LOCUST_TENANT"] = "lb"


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    import time

    environment.events.request.add_listener(lambda *args, **kw: time.sleep(0.1))
    StopUserOnFail(environment)


class login(RestUser):
    default_headers = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "sv,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    }

    @task
    def t(self):
        self.customer = next(self.customer_iterator)
        self.auth()
        with self.rest_(
            "GET", "/player/1/customizedsettings", headers={"accept": "application/json, text/javascript, */*; q=0.01"}
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://spela.test3.svenskaspel.se/",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://spela.test3.svenskaspel.se/logga-in/uppdaterade-villkor?returnUrl=%2F",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST", "/player/1/terms", headers={"accept": "application/json, text/javascript, */*; q=0.01"}, json={}
        ) as resp:
            pass
        with self.rest_(
            "GET",
            "/player/1/info?include=accountBalance",
            headers={"accept": "application/json, text/javascript, */*; q=0.01"},
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(login)
