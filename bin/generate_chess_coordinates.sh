#!/bin/sh

ruby -e '(1..8).reverse_each { |n| ("a".."h").each { |l| print "#{l}#{n} "}; print "\n"}'

