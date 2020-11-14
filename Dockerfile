FROM python:3.8.6
LABEL maintainers="brintly@gmail.com"


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -U pip && \
      pip install --no-cache-dir -r requirements.txt

COPY ytpl.py .

EXPOSE 5000
ENV FLASK_APP=ytpl.py
CMD [ "flask", "run", "--host=0.0.0.0" ]
