FROM python

WORKDIR /workdir
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python3", "./scripts/nba.py"]
