# Dockerfile
FROM python:3.5
WORKDIR /social
COPY social/ /social
COPY social/users /social/users
COPY social/manage.py /social
COPY social/social /social/social
COPY social/db.sqlite3 /social
COPY social/req.txt /social
RUN pip install -r /social/req.txt
#RUN python manage.py collectstatic --noinput
EXPOSE 8001
RUN cd /social
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
