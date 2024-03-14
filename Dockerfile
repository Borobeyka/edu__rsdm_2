FROM python:3.10

WORKDIR /part2

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

RUN ln -s /part2/src /usr/local/lib/python3.10/site-packages/

COPY . .