import xmlrpc.client

server = xmlrpc.client.ServerProxy('https://api.webfaction.com/');
session_id, account = server.login('piercegs', 'flysolo1', 'Web523', 2)
server.create_domain(session_id, 'xtendapp.com', 'superlists')
try:
    result = server.create_app(session_id, 'superlists', 'custom_app_with_port')
except xmlrpc.client.Fault:
    port = next(x['port'] for x in server.list_apps(session_id) if x['name'] == 'superlists')
else:
    port = result['port']
try:
    server.create_website(
        session_id,  # login session id
        'superlists',  # website name
        '207.38.86.218',  # website address
        False, # use http
        ['superlists.xtendapp.com'],  # domain
        '',  # ssl certificate (empty string means no ssl certificate)
        ['superlists', '/'], ['superlists_static', '/static']  # applications
    )
except xmlrpc.client.Fault:
    pass
print(f'port: {port}')