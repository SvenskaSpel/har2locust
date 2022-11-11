from locust import events
from locust_plugins.listeners import RescheduleTaskOnFail
from locust import task, run_single_user
from locust_plugins.users import RestUser


class NewName(RestUser):
    host = "https://api.spela.test3.svenskaspel.se/"
    default_headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "sv,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://spela.test3.svenskaspel.se",
        "pragma": "no-cache",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    }

    @task
    def t(self):
        with self.reader.user() as self.customer:
            with self.rest(
                "POST", "player/1/authenticate/testlogin", json={"personalId": self.customer["ssn"], "source": 3}
            ) as resp:
                pass


@events.init.add_listener
def renamed_function(environment, **_kwargs):
    RescheduleTaskOnFail(environment)


if __name__ == "__main__":
    run_single_user(NewName)
