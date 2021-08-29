This is a Python program that simulates sending emails to customers with provided template and content

## Usage

You can run it using terminal

```bash
python main.py ./email_template.json ./customers.csv ./output/ ./error.csv
```

Or using docker with the provided Dockerfile by running

```bash
docker build -t pi-exchange .
docker run -d pi-exchange
```

then you can access the Docker container's terminal that is running by

```bash
docker exec -it {{container_id}} bash
```

and check the result.
