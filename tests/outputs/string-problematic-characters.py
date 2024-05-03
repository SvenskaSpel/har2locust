from locust import FastHttpUser, run_single_user, task


class string_problematic_characters(FastHttpUser):
    host = "https://reqres.in"

    @task
    def t(self):
        with self.client.request(
            "PATCH",
            "/api/users/2",
            data='------WebKitFormBoundaryaVpJHMwCHF5PHRS7\r\nContent-Disposition: form-data; name="name"\r\n\r\n\'\\\'\\r\\n"\\"\r\n------WebKitFormBoundaryaVpJHMwCHF5PHRS7--\r\n',
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(string_problematic_characters)
