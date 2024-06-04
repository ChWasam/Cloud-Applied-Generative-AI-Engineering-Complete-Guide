FROM jupyter/base-notebook:latest
RUN pip install poetry
WORKDIR /code/
COPY . /code/
RUN poetry config virtualenvs.create false 
RUN poetry install 
EXPOSE 8888
CMD ["jupyter","notebook", "--port", "8888" ,"--no-browser", "--allow-root"]

# --no-browser:
# This option tells Jupyter Notebook not to open a web browser when it starts. This is useful in a containerized environment where opening a browser inside the container is not practical.

# --allow-root:

# This option allows Jupyter Notebook to be run as the root user. By default, Jupyter Notebook does not allow running as root for security reasons, but in a container, it is sometimes necessary.
