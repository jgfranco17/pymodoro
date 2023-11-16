# Project command runner
# Print list of available recipe (this)
default:
  @just --list

# Run pytest in system_tests_library
test *ARGS:
  pytest {{ARGS}} tests/. -vv
