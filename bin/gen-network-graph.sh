#!/bin/sh

# TODO handle deps better
# if this fails you must install graphviz

dot -Tsvg network.dot > network.svg
