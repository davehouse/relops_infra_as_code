import os
from google.cloud import logging


logging_client = logging.Client()

## limit to specific log:
#logger_name = os.environ.get('LOG_NAME', 'projects/dhouse-test/logs/gce_instance')
#logger = logging_client.logger(logger_name)
#print('Listing entries for logger {}:'.format(logger.name))
#for entry in logging_client.list_entries():
#    timestamp = entry.timestamp.isoformat()
#    print('* {}: {}'.format(timestamp, entry.payload))

for entry in logging_client.list_entries():
    timestamp = entry.timestamp.isoformat()
    print('* {}: {}'.format(timestamp, entry.payload))
