### To Build

    docker build -t test-boto3 .

### To run

     docker run -ti test-boto3 /scripts/gen_url.py

### Speed up development locally

     docker run -v `realpath ./scripts`:/tmp/scripts -ti test-boto3  /tmp/scripts/gen_url.py
