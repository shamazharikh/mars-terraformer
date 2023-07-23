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

# { docker buildx build -f Dockerfile \
#     --cache-from type=local,src=/mnt/d/GithubCache \
#     --cache-to type=local,dest=/mnt/d/GithubCache \
#     -t mazharshaikh/mars-terraformer:$TAG_PREFIX-$COMMIT_SHA . ; } >&2
{ docker build -f Dockerfile \
    -t mazharshaikh/mars-terraformer:$TAG_PREFIX-$COMMIT_SHA . ; } >&2
if [ $BRANCH == "main" ];
then
    docker push mazharshaikh/mars-terraformer:$TAG_PREFIX-$COMMIT_SHA
    docker tag mazharshaikh/mars-terraformer:$TAG_PREFIX-$COMMIT_SHA mazharshaikh/mars-terraformer:latest
    docker push mazharshaikh/mars-terraformer:latest
fi

printf "\n\n"
echo mazharshaikh/mars-terraformer:$TAG_PREFIX-$COMMIT_SHA
if [ $BRANCH == "master" ];
then
    echo mazharshaikh/mars-terraformer:latest
fi

TAG=$2
if [ -n "$TAG" ];
then
    echo "Tag used" >&2
    echo $TAG >&2
    docker tag mazharshaikh/mars-terraformer:$TAG_PREFIX-$COMMIT_SHA mazharshaikh/mars-terraformer:$TAG
    docker push mazharshaikh/mars-terraformer:$TAG
    echo mazharshaikh/mars-terraformer:$TAG
fi
