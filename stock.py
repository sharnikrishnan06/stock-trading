def stock_system(module):

    if module == "DATA":
        return "REAL-TIME DATA RECEIVED"

    elif module == "TRANSACTION":
        return "TRANSACTION VALIDATED"

    else:
        return "LOW LATENCY PERFORMANCE"


if __name__ == "__main__":

    module = input("Enter Module: ")

    print(stock_system(module))