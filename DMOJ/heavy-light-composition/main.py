num_strings, len_strings = map(int, input().split())

for x in range(num_strings):
    temp_cache = []
    strong_char = []
    user_input = input()
    is_strong_first = False

    # Check which characters are heavy
    for char in user_input:
        if char in temp_cache:
            strong_char.append(char)
        else:
            temp_cache.append(char)

    if user_input[0] in strong_char:
       is_strong_first = True

    # print(strong_char)

    for i in range(len(user_input)):
        if is_strong_first:
            if i % 2 == 0:
                if user_input[i] not in strong_char:
                    print("F")
                    break
            else:
                if user_input[i] in strong_char:
                    print("F")
                    break
        else:
            if i % 2 != 0:
                # print(user_input[i])
                if user_input[i] not in strong_char:
                    print("F")
                    break
            else:
                if user_input[i] in strong_char:
                    print("F")
                    break
        
        if i == len(user_input) - 1:
            print("T")
