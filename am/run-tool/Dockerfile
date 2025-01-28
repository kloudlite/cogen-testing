FROM python:alpine3.20
WORKDIR /app
COPY working/requirements.txt .
COPY am/requirements.txt builder-requirements.txt
RUN pip install -r requirements.txt
RUN pip install -r builder-requirements.txt
COPY . .
ARG TOOL_NAME
ENV TOOL_NAME=${TOOL_NAME}
CMD ["python", "am/run-tool/start.py"]