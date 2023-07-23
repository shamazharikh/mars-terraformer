set -eo pipefail

if [ "$#" -gt 2 ];
then
    echo "Usage bash build-docker-engine.sh <OPTIONAL branch name> <OPTIONAL TAG>"
    exit 126
fi

BASE_DOCKER_IMG=$1

if [ branch=$(git branch --show-current 2>/dev/null) ];
then
    # git version is old
    branch=$(git rev-parse --abbrev-ref HEAD)
fi

BRANCH=${2:-$branch}
echo "Branch for docker build" >&2
echo $BRANCH >&2

COMMIT_SHA=$(git rev-parse HEAD)
echo "Commit for docker build" >&2
echo $COMMIT_SHA >&2

TAG_PREFIX=$( [ $BRANCH == 'main' ] && echo "main" || echo "dev" )

{ docker build -f Dockerfile -t mars-terraformer:$TAG_PREFIX-$COMMIT_SHA . ; } >&2
if [ $BRANCH == "main" ];
then
    docker push mars-terraformer:$TAG_PREFIX-$COMMIT_SHA
    docker tag mars-terraformer:$TAG_PREFIX-$COMMIT_SHA mars-terraformer:latest
    docker push mars-terraformer:latest
fi

printf "\n\n"
echo mars-terraformer:$TAG_PREFIX-$COMMIT_SHA
if [ $BRANCH == "master" ];
then
    echo mars-terraformer:latest
fi

TAG=$2
if [ -n "$TAG" ];
then
    echo "Tag used" >&2
    echo $TAG >&2
    docker tag mars-terraformer:$TAG_PREFIX-$COMMIT_SHA mars-terraformer:$TAG
    docker push mars-terraformer:$TAG
    echo mars-terraformer:$TAG
fi
