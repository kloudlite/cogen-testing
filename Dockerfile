FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY app/agentman-0.0.2-py3-none-any.whl /app/agentman-0.0.2-py3-none-any.whl
COPY .tool_params.yaml /app/.tool_params.yaml
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt 
RUN pip install /app/agentman-0.0.2-py3-none-any.whl --force-reinstall

# Copy the rest of the files
COPY . .

# Set environment variable
ENV TOOL_PARAMS_FILE_PATH=.tool_params.yaml

# Expose the port
EXPOSE 4000

# Run the agent
CMD ["python", "-m", "agentman.run.agent", "agent"]
