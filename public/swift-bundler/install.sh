set -e

BRANCH=${1:-main}

# Create a temporary working directory
DIR=`mktemp -d`
cd $DIR

# Clone swift-bundler
echo ""
git clone https://github.com/stackotter/swift-bundler
cd swift-bundler
git checkout $BRANCH

# Install swift-bundler
echo "\nBuilding swift-bundler"
./install.sh

# Clean up
echo "\nCleaning up"
cd ../..
rm -rf $DIR
echo "Done"