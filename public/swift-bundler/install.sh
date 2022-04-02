set -e

# Create a temporary working directory
DIR=`mktemp -d`
cd $DIR

# Clone swift-bundler
echo ""
git clone https://github.com/stackotter/swift-bundler
cd swift-bundler

TAG=$(git describe --tags `git rev-list --tags --max-count=1`)
BRANCH=${1:-$TAG}
git -c advice.detachedHead=false checkout $BRANCH

# Install swift-bundler
./install.sh

# Clean up
echo "\nCleaning up"
cd ../..
rm -rf $DIR

echo "Done"
