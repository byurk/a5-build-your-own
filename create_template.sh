#!/bin/bash
# Script to create clean GitHub Classroom template

set -e  # Exit on error

echo "Creating clean template repository..."

# Navigate to parent directory
cd ..

# Remove old template if exists
if [ -d "a4-retrieval-kw-multiturn-template" ]; then
    echo "Removing existing template directory..."
    rm -rf a4-retrieval-kw-multiturn-template
fi

# Copy current repo to new directory
echo "Copying files..."
cp -r a4-retrieval-kw-multiturn-authoring a4-retrieval-kw-multiturn-template
cd a4-retrieval-kw-multiturn-template

# Remove git history
echo "Removing git history..."
rm -rf .git

# Remove CLAUDE-related files
echo "Removing CLAUDE files..."
rm -f CLAUDE.md

# Remove solutions directory (instructor only)
echo "Removing solutions directory..."
rm -rf solutions/

# Remove other workflows but keep classroom.yml for GitHub Classroom autograding
echo "Cleaning up workflows (keeping classroom.yml)..."
find .github/workflows -name '*.yml' ! -name 'classroom.yml' -delete 2>/dev/null || true

# Remove built/generated files
echo "Removing built/generated files..."
rm -rf .venv __pycache__ ai_in_loop/__pycache__ tests/__pycache__
rm -rf logs/ *.egg-info .pytest_cache
rm -rf ai_in_loop.egg-info

# Remove local environment files
echo "Removing local environment files..."
rm -f .env error.txt

# Remove this script from the template
rm -f create_template.sh

# Initialize fresh git repo
echo "Initializing fresh git repository..."
git init
git add .
git commit -m "Initial template for A4 RAG + Multi-turn Chat assignment"

echo ""
echo "Template created successfully!"
echo ""
echo "Next steps:"
echo "1. Go to https://github.com/new"
echo "2. Create repo: ai-in-the-loop-2026/a4-retrieval-kw-multiturn-template"
echo "3. Make it public"
echo "4. DO NOT initialize with README (we already have one)"
echo "5. Run these commands:"
echo ""
echo "   cd a4-retrieval-kw-multiturn-template"
echo "   git remote add origin git@github.com:ai-in-the-loop-2026/a4-retrieval-kw-multiturn-template.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
