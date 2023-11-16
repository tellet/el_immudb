import logging
import time
import requests
from requests import Response

from settings import API_PATH, IMMUDB_BASE_URL, X_API_KEY, COLLECTION, LEDGER

logger = logging.getLogger(__name__)

HEADERS = {
        'Accept': 'application/json',
        'X-API-Key': X_API_KEY,
        'Content-Type': 'application/json'
    }


def get_document_proof(document_id: str, transaction_id: int) -> Response:
    url = f'{IMMUDB_BASE_URL}/{API_PATH}/ledger/{LEDGER}/collection/{COLLECTION}/document/{document_id}/proof'
    data = {
        'transactionId': transaction_id
    }

    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 200:
        logger.info(f'{url} response is OK')
    else:
        logger.error(f'{url} response is: {response.status_code}, {response.text}')

    return response


def get_documents_count() -> Response:
    url = f'{IMMUDB_BASE_URL}/{API_PATH}/ledger/{LEDGER}/collection/{COLLECTION}/documents/count'
    data = {
        'limit': 0
    }

    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 200:
        logger.info(f'{url} response is OK')
    else:
        logger.error(f'{url} response is: {response.status_code}, {response.text}')

    return response


def add_document(event: str, api_key: str = X_API_KEY) -> Response:
    url = f'{IMMUDB_BASE_URL}/{API_PATH}/ledger/{LEDGER}/collection/{COLLECTION}/document'
    data = {
        'timestamp': int(time.time()),
        'ip': '127.0.0.1',
        'event': event
    }
    headers = {
        'Accept': 'application/json',
        'X-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        logger.info(f'{url} response is OK')
    else:
        logger.error(f'{url} response is: {response.status_code}, {response.text}')
    return response


def get_documents(page: int = 1, per_page: int = 100) -> Response:
    url = f'{IMMUDB_BASE_URL}/{API_PATH}/ledger/{LEDGER}/collection/{COLLECTION}/documents/search'
    data = {
        'page': page,
        'perPage': per_page
    }

    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 200:
        logger.info(f'{url} response is OK')
    else:
        logger.error(f'{url} response is: {response.status_code}, {response.text}')

    return response


if __name__ == '__main__':
    # for i in range(5):
    #     push_to_cloud('LOG IN')
    #     time.sleep(2)
    get_documents()
