FROM python:3.9
# Or any preferred Python version.

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./fruit_name_model.py"]
# Or enter the name of your unique directory and parameter set.