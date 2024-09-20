"""
    DOCS: File test calculate sum of two numbers
"""

def cal_sum(a:int|float, b:int|float):
    """_summary_

    Args:
        a (int | float): first number
        b (int | float): second number_

    Returns:
        int | float: sum of 2 numbers
    """
    return a + b


if __name__ == "__main__":
    print(cal_sum(3, 5))  # Output: 8
    print(cal_sum(3.5, 5.7))  # Output: 9.2
