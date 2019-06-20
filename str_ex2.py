#!/usr/bin/env python
from __future__ import print_function
my_var = input("enter an IP address")
my_var = my_var.split(".")
print("{:<12} {:<12} {:<12} {:<12}".format(*my_var))
