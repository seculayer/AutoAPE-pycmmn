# pycmmn

AutoAPE에서 사용하는 Python 공통 모듈

## 개발환경

- Python 3.7
- [Poetry](https://python-poetry.org)

## Python code format

```console
# black
poetry run black pycmmn tests

# isort
poetry run isort pycmmn tests
```

## 테스트

```console
poetry run pytest
```

또는 `poetry shell` 이후 `pytest` 명령어
