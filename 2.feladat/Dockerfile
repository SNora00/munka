FROM python:3.10-alpine

WORKDIR /app

RUN pip install zeep

COPY soap_calculator.py /app/

CMD ["python", "soap_calculator.py"]