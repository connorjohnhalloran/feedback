FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /flask_app
WORKDIR /flask_app
ADD requirements.txt /flask_app/
RUN pip install -r requirements.txt
ADD . /flask_app/
CMD ["python", "app.py" ]
