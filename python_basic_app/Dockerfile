# specify start image
FROM python:3.8

# adding the executable
ADD main.py .
ADD HR_Analytics.csv .

# installing dependencies
RUN pip install pandas

# set the start command
CMD [ "python", "./main.py"]