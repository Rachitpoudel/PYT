def compute_difference(list1, list2):
    diff1 = list(set(list1) - set(list2))
    diff2 = list(set(list2) - set(list1))
    return (diff1, diff2)

# Example usage
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
diff1, diff2 = compute_difference(color1, color2)
print("Color1-Color2:", diff1)
print("Color2-Color1:", diff2)
