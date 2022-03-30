FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py", "$ORG", "--name_filter", "$PATTERN", \
    "--pat", "$GITHUB_TOKEN", "--created_before", \
    "$CREATED_BEFORE", "--created_after", "$CREATED_AFTER" \
    ]