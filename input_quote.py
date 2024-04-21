def input_quote():
    input_string = input("Enter You Quote : ")

    # Split the input string at the comma character ","
    text_messages = input_string.split(", ")
    #print(text_messages)

    number_of_strings = len(text_messages)
    #print(f"There are {number_of_strings} strings in the list.")
    return number_of_strings , text_messages




