import requests

from common.api_common.logger import Log

logger = Log()


def requests_post(url, data=None, **kwargs):
    response = requests.post(url, data=data, **kwargs)
    if response.status_code < 400:
        if 'export' in url or 'template' in url:
            logger.info('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, '导出数据见导出文件'))
        else:
            logger.info('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))
    else:
        logger.error('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))

    return response


def requests_get(url, params=None, **kwargs):
    response = requests.get(url, params=params, **kwargs)
    if response.status_code < 400:
        if 'export' in url or 'template' in url:
            logger.info('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, '导出数据见导出文件'))
        else:
            logger.info('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))
    else:
        logger.error('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))

    return response


def requests_put(url, data=None, **kwargs):
    response = requests.put(url, data=data, **kwargs)
    if response.status_code < 400:
        logger.info('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))
    else:
        logger.error('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))
    return response


def requests_delete(url, **kwargs):
    response = requests.delete(url, **kwargs)
    if response.status_code < 400:
        logger.info('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))
    else:
        logger.error('url=%s，status_code=%s, request=%s，response=%s' % (url, response.status_code, data, response.text))
    return response


if __name__ == '__main__':
    url = 'http://t2niudun.fuyoukache.com/api/u/com/login.do'
    data = {
        'userName': 18514587147,
        'password': 'Fy123456789',
        'checkRequestId': '',
        'checkCodeValue': '',
        'role': 1
    }
    r = requests_post(url, data)
    print(r.json())
    cookies = r.cookies.get_dict()
    print(cookies)
    url = 'http://t2niudun.fuyoukache.com/api/supplier/account/getAllSupplierInfo123.do'
    r = requests_post(url, cookies=cookies)
    print(r)
    r = requests_get(url, cookies=cookies)
    print(r)
