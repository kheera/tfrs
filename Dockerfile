FROM python:2-onbuild

EXPOSE 9000

ENTRYPOINT ["./docker-entrypoint.sh"]

#CMD [ "python", "manage.py", "runserver", "0.0.0.0:9000" ]
