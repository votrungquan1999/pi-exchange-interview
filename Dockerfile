FROM python:3 as work_dir
WORKDIR /usr/src
COPY . .
RUN python main.py ./email_template.json ./customers.csv ./output/ ./error.csv
CMD tail -f /dev/null