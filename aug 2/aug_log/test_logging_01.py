import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')