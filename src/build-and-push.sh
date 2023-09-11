docker build . --tag fastapi

docker tag fastapi us-east1-docker.pkg.dev/bhdigital-data-dev/asset-transfer-artifact-registry-dev/fastapi-np-test

docker push us-east1-docker.pkg.dev/bhdigital-data-dev/asset-transfer-artifact-registry-dev/fastapi-np-test
