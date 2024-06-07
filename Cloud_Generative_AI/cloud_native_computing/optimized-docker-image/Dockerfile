Single-Stage Build

FROM python:3.12
RUN pip install poetry 
LABEL  maintainer = "ch.wasam@gmail.com"
WORKDIR  /copy/
ADD . /copy/
RUN poetry config virtualenvs.create false
RUN poetry install 
EXPOSE 8000
CMD ["poetry", "run", "uvicorn" ,"app.main:app", "-p" ,"0.0.0.0" ,"--reload"]

# docker images with big size would be slow, more potential vulnerabilities and bigger attack service.


# We can use the technique i.e. Multi-Stage Build to reduce the image size
# significantly. In this technique, we only keep that stuff in the image which needs to
# run the application in production.