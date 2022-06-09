import azure.cosmos.cosmos_client as cosmos_client
import datetime

settings = {
    'host': 'https://group1.documents.azure.com:443/',
    'master_key':  '1S1uClbA0fMsy1rxUIf4cqpr2jKqP3dQRCR1BUwlSEjFBfZFXJdjS15s3vfnJki7NEpXfzuVDrycZP6BibxMtA==',
    'database_id':  'TodolistDatabase',
    'container_id':  'Todolist'
}

HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']
CONTAINER_ID = settings['container_id']


def read_items(container):
    print('\nReading all items in a container\n')
    item_list = list(container.read_all_items(max_item_count=10))
    print('Found {0} items'.format(item_list.__len__()))
    return item_list

def create_items(container, item_id, log_text):
    print('\nInserting log\n')
    log_text = str(log_text)
    date_and_time = str(datetime.datetime.now())
    final_log = {
        'id' : item_id,
        'log': log_text,
        'datetime': date_and_time  }
    print(final_log)
    container.create_item(body=final_log)


def insert_log(log_text):
    client = cosmos_client.CosmosClient(HOST, \
                                        {'masterKey': MASTER_KEY},
                                        user_agent="CosmosDBPythonQuickstart",
                                        user_agent_overwrite=True)
    db = client.get_database_client(DATABASE_ID)
    container = db.get_container_client(CONTAINER_ID)

    items = read_items(container)
    new_item_id = str(len(items)+1)

    create_items(container, new_item_id, log_text)
