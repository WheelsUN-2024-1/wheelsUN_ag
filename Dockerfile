FROM python:3.12.2-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8100

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8100", "--reload" ]