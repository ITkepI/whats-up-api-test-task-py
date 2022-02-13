import webbrowser
from requests import get as GET
from requests import post as POST
from time import sleep as wait


def create_url(url_base, method):

    return f'{url_base}/{method}'


def status_check(status_need, url_base, chat_token, wait_time):

    url = f'{url_base}/status'
    chat = GET(url, 
        params={'token': chat_token, 'full': '1'}, 
        headers={'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
        ).json()
    print(chat)
    while (chat['state'] != status_need):
        print(f'Status is "{chat["state"]}". Status have to be "{status_need}"')
        chat = GET(url, params=query_params, headers=HEADER).json()
        wait(wait_time)


api_server = 'https://dev.wapp.im/v3'
HEADER = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}

# параметры для получения свободного чата
url = f'{api_server}/chat/spare'
query_params = {'crm': 'TEST', 
                'domain': 'test'}

# получаем свободный чат
free_chat = GET(url, params=query_params, headers=HEADER).json()
print(free_chat, end='\n\n')

# получаем ID и TOKEN (записываем данные в базу)
personal_id = 19
chat_token = 'lTsange7Fg8RBI8u'

# personal_id = free_chat['id']
# chat_token = free_chat['token']

url_base = f'{api_server}/instance{personal_id}'

# инициализируем чат и дожидаемся статуса "got qr code"
status_check('got qr code', url_base, chat_token, wait_time=0.5)

# получаем qr код в виде картинки
query_params = {'token': chat_token}
url = create_url(url_base, method='qr_code')
qr_picture = GET(url, params=query_params, headers=HEADER)

with open('qr.html', 'wb+') as qr_code:
    qr_code.write(qr_picture.content)
webbrowser.open('qr.html')

# сканируем qr код вручную

# получаем статус, что whatsup подключён
# т.к. нужно дождаться сканирования qr, то время ожидания можно выставить побольше
status_check('CONNECTED', url_base, chat_token, wait_time=2)

print('You good!')

# отправляю сообщение
url = create_url(url_base, method='sendMessage')
phone = '89872745052'
# записываю имя и телефон в сообщение
name = 'A'
surname = 'T'
my_phone = '89811111111'
message = f'{name} {surname} {my_phone}'
POST(url, params=query_params, headers=HEADER, json={'phone': phone, 'body': message})