FROM python:3
ADD app.py /
ADD weather.py /
ADD requirements.txt /
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "./app.py" ]
