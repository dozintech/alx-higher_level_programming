#!/usr/bin/fish

# Example: run_d_test 0
#   Tests the doctest in ./tests/0-add_integer.txt
function run_d_test
    if test (count $argv) -eq 1
        python3 -m doctest -v ./tests/$argv[1]-*
    end
end
