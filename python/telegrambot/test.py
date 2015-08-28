import time
import requests
requests.packages.urllib3.disable_warnings()
URL = 'https://api.telegram.org/bot'
TOKEN = ''
INTERVAL = 5
ADMIN_ID = 130318030
def check_updates(offset):
    data = {'offset': offset + 1, 'limit': 5, 'timeout': 0}
    try:
        request = requests.post(URL + TOKEN + '/getUpdates', data = data)
    except Exception as e:
        print e
        return offset
    if not request.status_code == 200: return offset
    if not request.json()['ok']: return offset
    for update in request.json()['result']:
        offset = update['update_id']
        if not 'message' in update:
            print "Unknown message"
        else:
            from_id = update['message']['chat']['id']
            if from_id == ADMIN_ID:
                req = {'chat_id': from_id, 'text': 'You said %s' % update['message']['text']}
                requests.post(URL + TOKEN + '/sendMessage', data = req)
                if not request.status_code == 200:
                    print request.status_code
            print from_id
    return offset

if __name__ == "__main__":
    offset = 0
    while True:
        try:
            offset = check_updates(offset)
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print 'Interrupted by user'
            break
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
