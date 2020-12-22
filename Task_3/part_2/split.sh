# 33,80,603 total number of lines

# Show all file since line 'num':
#     tail -n +num file

# echo "$(tail -n +3 Posts.xml)" >Posts.xml

# Output everything but the last few lines of a file:
#     head -n -count_of_lines filename
# echo "$(head -n -1 Posts.xml)" >Posts.xml

split -l 80000 --numeric-suffixes  "Posts.xml" file_obj

