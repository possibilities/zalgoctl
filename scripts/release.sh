#!/usr/bin/env bash
set -euo pipefail

# Release script for zalgoctl
# Usage: ./scripts/release.sh <version>
# Example: ./scripts/release.sh 0.2.0

VERSION="${1:-}"

if [[ -z "$VERSION" ]]; then
    echo "Usage: $0 <version>"
    echo "Example: $0 0.2.0"
    exit 1
fi

# Validate version format (basic semver)
if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Error: Version must be in semver format (e.g., 0.2.0)"
    exit 1
fi

echo "Releasing zalgoctl v$VERSION..."

# Update version in pyproject.toml
sed -i '' "s/^version = \".*\"/version = \"$VERSION\"/" pyproject.toml
echo "Updated pyproject.toml to version $VERSION"

# Clean previous builds
rm -rf dist/

# Build the package
echo "Building package..."
uv build

# Publish to PyPI
echo "Publishing to PyPI..."
uv run twine upload dist/*

# Create and push git tag
echo "Creating git tag..."
git add pyproject.toml
git commit -m "release: v$VERSION"
git tag -a "v$VERSION" -m "Release v$VERSION"
git push origin main
git push origin "v$VERSION"

echo "Released zalgoctl v$VERSION"
