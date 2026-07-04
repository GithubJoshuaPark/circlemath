#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting deployment to circlemath..."

# 1. Build
echo "📦 Building the project..."
# Load NVM if available
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
    . "$NVM_DIR/nvm.sh"
    nvm use 22.22.2
else
    echo "⚠️ NVM not found at $NVM_DIR/nvm.sh, skipping nvm use..."
fi
npm run build

# 2. Deploy
echo "☁️ Deploying to Firebase Hosting (circlemath)..."
firebase deploy --only hosting:circlemath

echo "✅ Deployment complete! Check https://circlemath.web.app/"
