#!/usr/bin/env python3
from locust import FastHttpUser, task, run_single_user, events
from locust_plugins.listeners import RescheduleTaskOnFail


class MyUser(FastHttpUser):
    host = "https://nowhere"

    @task
    def t(self):
        self.client.get("https://reqres.in/api/users?page=2")
        self.client.post(
            "https://reqres.in/api/users",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "sv,en;q=0.9",
                "content-type": "application/json",
                "origin": "https://reqres.in",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            },
            data='{"name":"morpheus","job":"leader"}',
        )
        self.client.patch(
            "https://reqres.in/api/users/2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "sv,en;q=0.9",
                "content-type": "application/json",
                "origin": "https://reqres.in",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            },
            data='{"name":"morpheus","job":"zion resident"}',
        )
        self.client.delete(
            "https://reqres.in/api/users/2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "sv,en;q=0.9",
                "content-type": "application/json",
                "origin": "https://reqres.in",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            },
        )


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    RescheduleTaskOnFail(environment)


if __name__ == "__main__":
    run_single_user(MyUser)
