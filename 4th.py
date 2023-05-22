''' Program to compare three lists '''

def compare_lists(list1, list2, list3):

  if len(list1) != len(list2) or len(list1) != len(list3):
    return False

  for i in range(len(list1)):
    if list1[i] != list2[i] or list1[i] != list3[i]:
      return False

  return True


if __name__ == "__main__":
  list1 = [1, 2, 3, 4, 5]
  list2 = [1, 2, 3, 4, 5]
  list3 = [1, 2, 3, 4, 5]

  if compare_lists(list1, list2, list3):
    print("The lists are equal.")
  else:
    print("The lists are not equal.")