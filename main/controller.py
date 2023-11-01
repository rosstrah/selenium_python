import os
import random
from aiohttp import web
import traceback
from aiohttp.web_exceptions import HTTPForbidden
from multidict import MultiDict
import tempfile
import subprocess
from main.seleniumApi import SeleniumApi

token = 'dfhiwhu84739hr393b9r3yy'


async def selenium_screenshot(request):
    try:
        reader = await request.multipart()

        if request.headers.get('AUTHORIZATION') is None or request.headers.get('Authorization') != token:
            raise HTTPForbidden()

        url = 'mail.ru'
        pict_name = 'default.png'

        # читаем поля формы
        while True:
            part = await reader.next()
            if part is None: break

            if part.name == 'url':
                url = (await part.read(decode=True)).decode()
            if part.name == 'pict_name':
                pict_name = (await part.read(decode=True)).decode()
                pict_name = pict_name + '.png'

        # запускаем скрипт
        api = SeleniumApi()
        res = api.get_screenshot(url, pict_name)

        if res:
            return web.Response(text='Изображение сохранено в: tmp/' + pict_name + '', status=200)

        return web.Response(text='Ошибка обработки изображения', status=400)
    except ValueError:
        return web.Response(text=str(traceback.format_exc()), status=500)


async def test(request):
    try:
        reader = await request.multipart()

        if request.headers.get('AUTHORIZATION') is None or request.headers.get('Authorization') != token:
            raise HTTPForbidden()

        hashToCode = ''

        # читаем поля формы
        while True:
            part = await reader.next()
            if part is None: break

            if part.name == 'hashToCode':
                hashToCode = (await part.read(decode=True)).decode()

        return web.Response(text='Все оки доки ' + hashToCode, status=200)
    #            return web.Response(text='Ошибка : '+res['error'], status=400)
    except ValueError:
        return web.Response(text=str(traceback.format_exc()), status=500)


async def screenshot(request):
    try:
        reader = await request.multipart()

        if request.headers.get('AUTHORIZATION') is None or request.headers.get('Authorization') != token:
            raise HTTPForbidden()

        url = 'mail.ru'

        # читаем поля формы
        while True:
            part = await reader.next()
            if part is None: break

            if part.name == 'url':
                url = (await part.read(decode=True)).decode()

        # запускаем скрипт
        command = "google-chrome-stable --headless --no-sandbox --screenshot https://www." + url + "/"
        ## command = "ls -l ./"
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print(result.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            # error ino
            print(f"Error: {e.output.decode('utf-8')}")

        return web.Response(text='Скриншот сделан', status=200)
    #            return web.Response(text='Ошибка : '+res['error'], status=400)
    except ValueError:
        return web.Response(text=str(traceback.format_exc()), status=500)


async def getHtml(request):
    try:
        reader = await request.multipart()

        if request.headers.get('AUTHORIZATION') is None or request.headers.get('Authorization') != token:
            raise HTTPForbidden()

        url = 'mail.ru'

        # читаем поля формы
        while True:
            part = await reader.next()
            if part is None: break

            if part.name == 'url':
                url = (await part.read(decode=True)).decode()

        # запускаем скрипт
        command = "google-chrome-stable --headless --no-sandbox --dump-dom https://www." + url + "/"
        result = 'ошибка'
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print(result.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            # error ino
            print(f"Error: {e.output.decode('utf-8')}")

        return web.Response(text=result.decode('utf-8'), status=200)
    #            return web.Response(text='Ошибка : '+res['error'], status=400)
    except ValueError:
        return web.Response(text=str(traceback.format_exc()), status=500)


async def selenium_console_command(request):
    try:
        reader = await request.multipart()

        if request.headers.get('AUTHORIZATION') is None or request.headers.get('Authorization') != token:
            raise HTTPForbidden()

        url = 'https://mail.ru'
        console_command = 'console.log("Hi")'

        # читаем поля формы
        while True:
            part = await reader.next()
            if part is None: break

            if part.name == 'url':
                url = (await part.read(decode=True)).decode()
            if part.name == 'console_command':
                console_command = (await part.read(decode=True)).decode()

        # запускаем скрипт
        api = SeleniumApi()
        res = api.execute_console_command(url, console_command)

        if res:
            return web.Response(text='Команда выполнена' + res + '', status=200)

        return web.Response(text='Ошибка выполнения команды', status=400)
    except ValueError:
        return web.Response(text=str(traceback.format_exc()), status=500)
