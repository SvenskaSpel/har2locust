from locust import FastHttpUser, run_single_user, task


class url_encoded_body_no_text_field(FastHttpUser):
    host = "https://reqres.in"
    default_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    @task
    def t(self):
        with self.client.request("POST", "/api/users", data="user=test&password=test", catch_response=True) as resp:
            pass


if __name__ == "__main__":
    run_single_user(url_encoded_body_no_text_field)
