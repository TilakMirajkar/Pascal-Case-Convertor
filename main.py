str_input = input("Enter your text: ").split()
capitalized_list = [strs[0].upper() + strs[1:] if strs else '' for strs in str_input]
print(' '.join(capitalized_list))