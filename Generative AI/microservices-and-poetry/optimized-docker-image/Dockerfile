FROM python:3.12
RUN pip install poetry 
LABEL  maintainer = "ch.wasam@gmail.com"
WORKDIR  /copy/
ADD . /copy/
RUN poetry config virtualenvs.create false
RUN poetry install 
EXPOSE 8000
CMD ["poetry", "run", "uvicorn" ,"app.main:app", "-p" ,"0.0.0.0" ,"--reload"]