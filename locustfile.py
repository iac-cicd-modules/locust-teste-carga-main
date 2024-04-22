from locust import HttpUser, task, between
import logging


class ApiUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        logging.basicConfig(level=logging.INFO)

    headers = {
        "x-hubly-key": "f7bc2b123991ae43d6a38cdfcbe77d52522d923cc5d289cafe3ffbf7530fe500"
    }

    @task
    def post_inside_sales(self):
        try:
            body = {
              "consultantId": "GN5913",
              "skus": [
                {
                  "id": "10225720",
                  "quantity": 1
                }
              ]
            }

            response = self.client.post(
                "/api/insideSales",
                json=body,
                headers=self.headers,
                name="Inside Sales API")

            logging.info(f'response URL: {response.url}')
            logging.info(f'response status code: {response.status_code}')
            logging.info(f'response text: {response.text}')
            logging.info('------------------------------------------------------------')
        except Exception as e:
            logging.error(e)
