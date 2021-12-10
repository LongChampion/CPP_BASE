#!/usr/bin/env python3

from os import system as RunCommand

# Check files to run
CHECK = [
    "-*",
    "bugprone-*",
    "cert-*",
    "clang-analyzer-*",
    "concurrency-*",
    "cppcoreguidelines-*",
    "-cppcoreguidelines-avoid-magic-numbers",
    "hicpp-*",
    "-hicpp-braces-around-statements",
    "-hicpp-named-parameter",
    "misc-*",
    "modernize-*",
    "-modernize-use-trailing-return-type",
    "portability-*",
    "readability-*",
    "-readability-braces-around-statements",
    "-readability-function-cognitive-complexity",
    "-readability-magic-numbers",
    "-readability-named-parameter",
]

if "__main__" == __name__:
    COMMAND = 'clang-tidy --checks="{}" --dump-config >| .clang-tidy'.format(','.join(CHECK))
    print("[+] Run command: {}".format(COMMAND))
    RunCommand(COMMAND)
    print("[+] Done!")
