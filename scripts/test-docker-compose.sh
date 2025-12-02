#!/usr/bin/env bash

set -e # Exit on error
set -u # Exit on undefined variable

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
log_info() {
  echo -e "${GREEN}[INFO]${NC} $1"
}

log_error() {
  echo -e "${RED}[ERROR]${NC} $1"
}

log_warning() {
  echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Cleanup function
cleanup() {
  log_info "Cleaning up..."
  docker compose down -v --remove-orphans
}

# Set trap to cleanup on exit
trap cleanup EXIT

# Main test flow
main() {
  log_info "Starting Docker Compose tests..."

  # Build the images
  log_info "Building Docker images..."
  docker compose build

  # Ensure clean state
  log_info "Ensuring clean state..."
  docker compose down -v --remove-orphans

  # Start services
  log_info "Starting services..."
  docker compose up -d --wait my-app

  # Wait a bit for service to be fully ready
  log_info "Waiting for service to be ready..."
  sleep 2

  # Test liveness endpoint
  log_info "Testing liveness endpoint..."
  response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/v1/healthcheck/liveness)

  if [ "$response" = "200" ]; then
    log_info "✓ Liveness endpoint test passed (HTTP $response)"
  else
    log_error "✗ Liveness endpoint test failed (HTTP $response)"
    log_info "Showing container logs:"
    docker compose logs my-app
    exit 1
  fi

  log_info "All tests passed successfully! ✓"
}

# Run main function
main
