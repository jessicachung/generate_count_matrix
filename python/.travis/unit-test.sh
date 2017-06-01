#!/bin/bash

set -e
errors=0

# Run unit tests
python python/generate-count-matrix/generate-count-matrix_test.py || {
    echo "'python python/generate-count-matrix/generate-count-matrix_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E python/generate-count-matrix || {
    echo "'pylint -E python/generate-count-matrix' failed"
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
