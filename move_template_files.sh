#!/bin/sh

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh oasis_optimal_footer_pages/ .
  rm -rfv oasis_optimal_footer_pages
fi
