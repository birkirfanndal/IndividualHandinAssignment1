
def add(numbers):
    if numbers == "":
        return "0"
    elif "," not in numbers:
        return str(numbers)
    elif "," in numbers:
        num_list = numbers.split(",")
        num_sum = 0
        for i in num_list:
            num_sum += int(i)
        return str(num_sum)