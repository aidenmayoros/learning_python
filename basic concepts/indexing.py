# indexing = accessing elements of a sequence using []
# [start : end : step]

credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[0])  # returns 1
print(credit_card_number[:4])  # returns 1234 - first 4 elements
print(credit_card_number[5:9])  # returns 5678 - elements from place 5 to 9
print(credit_card_number[5:])  # returns 5678-9012-3456 - elements from 5 to end
print(credit_card_number[-1])  # returns 6 - last element
print(credit_card_number[::3])  # returns 146-136 - return all elements skipping 3
