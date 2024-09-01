#!/bin/bash

container_name=doc-powered-rag

function build() {

  echo "Building Images"
  if [ "$(docker ps | (grep -q $container_name))" ] && [ "$(docker container insepct -f '{{.State.Running}}' $container_name)" = "true" ] ; then
    echo "Killing container"
    (docker kill $container_name || :)

  fi

  #clean docker cache
  docker rmi --force $container_name

  docker build . -t $container_name


  returnValue=$?

  if [ $returnValue -ne 0 ]; then
    echo "Error while building the image"
    exit $returnValue

  fi

}

function docker_run() {

  pid=$(docker ps -a | grep $container_name | awk '{print $1}')

  if [[ -n "$pid" ]]; then
    echo "Killing running instances; "
    docker rm -f "$pid"
  fi
  docker run -d --name $container_name $container_name

  echo "---------------------------------------"
  echo "[INFO] server running on http://localhost:8080"
  echo "________________________________________"
}


function run_tests() {
    echo "Running Integration Tests"
    docker exec $container_name sh -c "python3 -m pytest"


}

build
docker_run
run_tests

