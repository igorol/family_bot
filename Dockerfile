FROM python:3
ARG telegram_bot_token
ENV telegram_bot_token=${telegram_bot_token}
ADD app.py /
ADD weather.py /
ADD requirements.txt /
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "./app.py" ]
