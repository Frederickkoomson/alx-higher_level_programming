#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            division_result = value_1 / value_2
            if not isinstance(division_result, (int, float)):
                raise TypeError
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        else:
            result.append(division_result)
        finally:
            pass
    return result
