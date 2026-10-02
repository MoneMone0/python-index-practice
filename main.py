# 기존 코드: 목록 범위를 벗어나 IndexError 발생
# def last_item(items):
#     return items[len(items)]
#
# print(last_item(["apple", "banana", "cherry"]))


# 수정 코드: 빈 목록을 처리하고 마지막 항목 반환
def last_item(items):
    if not items:
        return None
    return items[-1]


print(last_item(["apple", "banana", "cherry"]))  # cherry
print(last_item([]))                            # None
