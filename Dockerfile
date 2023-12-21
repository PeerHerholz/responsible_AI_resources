FROM python:3.10

# make dir for Dash app python code
RUN mkdir /RAI_resources_dash_app
ADD . /RAI_resources_dash_app
RUN chmod -R 755 /RAI_resources_dash_app
WORKDIR /RAI_resources_dash_app

RUN pip install -r requirements.txt

EXPOSE 7860

# the -u option means it's executed as 'unbuffered' which means all print statements are sent to std.out, which means they're printed in docker-compose (use for debugging)
CMD ["python", "-u", "app.py"]