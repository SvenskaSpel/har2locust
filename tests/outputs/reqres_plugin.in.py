from locust import task, run_single_user, events
from locust_plugins.listeners import RescheduleTaskOnFail
from locust_plugins.users import RestUser


class NewName(RestUser):
    host = "https://reqres.in/"
    default_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "sv,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://reqres.in",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }

    @task
    def renamed_function(self):
        with self.rest("POST", "api/users", json={"name": "morpheus", "job": "leader"}) as resp:
            pass


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    RescheduleTaskOnFail(environment)


if __name__ == "__main__":
    run_single_user(reqres_in)
