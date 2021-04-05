
def calculate(num_1, num_2, operation):
    if operation == "+":
        answer = num_1 + num_2 
    elif operation == "-":
        answer = num_1 - num_2 
    elif operation == "*":
        answer = num_1 * num_2 
    elif operation == "/":
        answer = num_1 / num_2 
    return answer 

def print_operations():
    print("+\n-\n*\n/")

def use_running_answer(running_answer):
    first_number = running_answer 
    print_operations()
    operation = input("Choose an operation: ")
    second_number = int(input("What is the second number? "))
    return calculate(first_number, second_number, operation)  

def use_fresh_inputs():
    first_number = int(input("What is the first number? "))
    print_operations()
    operation = input("Choose an operation: ")
    second_number = int(input("What is the second number? "))
    return calculate(first_number, second_number, operation)

def calculator():
    running_answer = use_fresh_inputs()
    print(running_answer)
    while(True):
        use_running_answer_or_not = input("Continue with last answer? Type 'yes' or 'no': ")
        if use_running_answer_or_not == 'yes':
            running_answer = use_running_answer(running_answer)
            print(running_answer)
            continue
        else:
            running_answer = use_fresh_inputs()
            print(running_answer)
            continue

calculator()