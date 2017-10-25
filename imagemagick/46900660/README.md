1. Build the docker images

    docker build  -t imagemagick-pdf .


2. Run the docker image this way

    docker run -v `pwd`:/output -ti imagemagick-pdf  bash /run.sh 
