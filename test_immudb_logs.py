import pytest

from immudb_logs import get_documents_count, add_document, get_documents, get_document_proof
from utils import parse_json


class TestImmuDBLogs:
    def test_add_document_response_is_200(self):
        resp = add_document('test event')
        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
        response = parse_json(resp.text)
        assert response.get('transactionId', None) is not None, f'transactionId is not found in response {resp.text}'
        assert response.get('documentId', None) is not None, f'documentId is not found in response {resp.text}'

    def test_get_documents_count_response_is_200(self):
        resp = get_documents_count()
        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
        response = parse_json(resp.text)
        assert response.get('collection', None) is not None, f'collection is not found in response {resp.text}'
        assert response.get('count', None) is not None, f'count is not found in response {resp.text}'

    def test_get_documents_response_is_200(self):
        resp = get_documents(1, 100)
        if resp.status_code != 200 and 'empty' in resp.text:
            pytest.skip(f'DB is empty: {resp.status_code}, {resp.text}')

        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
        response = parse_json(resp.text)
        assert response.get('searchId', None) is not None, f'searchId is not found in response {resp.text}'
        assert response.get('revisions', None) is not None, f'revisions is not found in response {resp.text}'
        assert response.get('page', None) == 1, f'page is not found in response {resp.text}'
        assert response.get('perPage', None) == 100, f'perPage is not found in response {resp.text}'

    def test_get_documents_shows_2nd_page_ok(self):
        resp = get_documents(2, 1)
        if resp.status_code != 200 and 'empty' in resp.text:
            pytest.skip(f'DB is empty: {resp.status_code}, {resp.text}')

        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
        response = parse_json(resp.text)
        assert len(response.get('revisions', [])) == 1, f'unexpected items count in revisions {resp.text}'
        assert response.get('page', None) == 2, f'unexpected page in response {resp.text}'
        assert response.get('perPage', None) == 1, f'unexpected perPage in response {resp.text}'

    def test_pushed_log_line_appears_in_db(self):
        # store the initial amount of documents in the collection
        resp = get_documents_count()
        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
        response = parse_json(resp.text)
        initial_count = response.get('count', 0)

        # push a log line
        resp = add_document('test event')
        if resp.status_code != 200:
            pytest.skip(f'Failed to push log line: {resp.status_code}, {resp.text}')
        response = parse_json(resp.text)
        document_id = response.get('documentId', None)
        transaction_id = response.get('transactionId', None)

        # assert count of items increased
        resp = get_documents_count()
        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
        response = parse_json(resp.text)
        new_count = response.get('count', 0)
        assert new_count - initial_count == 1
        # assert document was created
        resp = get_document_proof(document_id, transaction_id)
        assert resp.status_code == 200, f'Unexpected status code received: {resp.status_code}, {resp.text}'
