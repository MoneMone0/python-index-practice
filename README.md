# Python Index Practice

Python 목록의 인덱스를 공부하는 연습 저장소입니다.
학습을 위해 의도적으로 오류가 있는 코드를 포함합니다.

## 실행

```bash
python main.py
```

## 현재 코드의 문제

마지막 항목을 가져오려고 `items[len(items)]`를 사용했지만,
목록 범위를 벗어나 `IndexError: list index out of range`가 발생합니다.

## 원하는 동작

- 항목이 있으면 마지막 항목을 반환
- 빈 목록이면 `None`을 반환
