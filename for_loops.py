# for loops execute a block of code a set number of times.
# Can itterate over range, string, sequence ect.

# for x in range(1, 11):
#     print(x)

for x in range(1, 21):
    if x == 13:
        continue  # skip this itteration and go to the next
        # break will stop the loop completly
    else:
        print(x)
