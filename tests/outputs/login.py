from locust import task, run_single_user, events
from locust_plugins.listeners import RescheduleTaskOnFail
from locust_plugins.users import RestUser


class login(RestUser):
    host = "https://api.spela.test3.svenskaspel.se/"
    default_headers = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "sv,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    }

    @task
    def t(self):
        with self.rest(
            "POST",
            "player/1/authenticate/testlogin",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "origin": "https://spela.test3.svenskaspel.se",
            },
            json={"personalId": "193804122491", "source": 3},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "player/1/customizedsettings?_=1636025335990",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "origin": "https://spela.test3.svenskaspel.se",
            },
        ) as resp:
            pass
        with self.client.get(
            "https://spela.test3.svenskaspel.se/",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(
            "https://spela.test3.svenskaspel.se/logga-in/uppdaterade-villkor?returnUrl=%2F",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST",
            "player/1/terms",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "origin": "https://spela.test3.svenskaspel.se",
            },
            json={},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "player/1/info?include=accountBalance&_=1636025343876",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "origin": "https://spela.test3.svenskaspel.se",
            },
        ) as resp:
            pass


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    RescheduleTaskOnFail(environment)


if __name__ == "__main__":
    run_single_user(login)
