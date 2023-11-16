import json
import logging
from json import JSONDecodeError

logger = logging.getLogger(__name__)


def parse_json(content) -> dict:
    resp_content = ''
    try:
        resp_content = json.loads(content)
    except JSONDecodeError as er:
        logger.error(f'Failed to decode {content}, {er}')
    except TypeError as er:
        logger.error(f'Failed to parse {content}, {er}')
    return resp_content
