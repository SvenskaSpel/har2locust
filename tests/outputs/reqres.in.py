from locust import FastHttpUser, run_single_user, task


class reqres_in(FastHttpUser):
    host = "https://reqres.in"
    default_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "sv,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://reqres.in",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }

    @task
    def t(self):
        with self.rest("POST", "/api/users", json={"name": "morpheus", "job": "leader"}) as resp:
            pass
        with self.rest("PATCH", "/api/users/2", json={"name": "morpheus", "job": "zion resident"}) as resp:
            pass
        with self.client.request("DELETE", "/api/users/2", catch_response=True) as resp:
            pass


if __name__ == "__main__":
    run_single_user(reqres_in)
