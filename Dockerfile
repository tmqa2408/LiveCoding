FROM python

# Установка Chromium и необходимых зависимостей


# Возврат к обычному пользователю, если нужно


# Установка рабочей директории
WORKDIR /usr/workspace

# Копирование зависимостей и установка Python пакетов
COPY ./requirements.txt .
RUN mkdir allure-results
RUN pip install -r requirements.txt
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

CMD ["pytest"]