import sys

# When I run this program using one of the following command,
#       - python 03_command_line_input.py 2023-11-08
#       - python3 03_command_line_input.py 2023-11-08

# The output is as follows:

print(sys.argv)  # output : ['03_command_line_input.py', '2023-11-08']
print(sys.argv[0])  # output : 03_command_line_input.py
print(sys.argv[1])  # output : 2023-11-08