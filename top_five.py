def highFive(items):
    students = dict()
    output = []
    for item in items:
        if item[0] not in students:
            students[item[0]] = [item[1]]
        else:
            students[item[0]].append(item[1])

    for items in sorted(students.items()):
        output.append([items[0], sum(sorted(items[1], reverse=True)[:5]) // 5])
    return output


if __name__ == '__main__':
    print(highFive([[5, 91], [5, 92], [3, 93], [3, 97], [5, 60], [
          3, 77], [5, 65], [5, 87], [5, 100], [3, 100], [3, 76]]))
