docker build . --tag fastapi-np-test-app

docker tag fastapi-np-test-app us-east1-docker.pkg.dev/bhdigital-data-dev/asset-transfer-artifact-registry-dev/fastapi-np-test

docker push us-east1-docker.pkg.dev/bhdigital-data-dev/asset-transfer-artifact-registry-dev/fastapi-np-test
