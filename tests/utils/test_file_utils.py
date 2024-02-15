import io
import uuid
from pathlib import Path

import pytest

from pycmmn.utils.FileUtils import FileUtils


@pytest.fixture
def pathname1(tmp_path) -> Path:
    return tmp_path / str(uuid.uuid4())


@pytest.fixture
def pathname2(tmp_path) -> Path:
    return tmp_path / str(uuid.uuid4())


def test_mkdir(pathname1):
    FileUtils.mkdir(pathname1)
    assert pathname1.exists()


@pytest.mark.exception
def test_mkdir_with_existed_file(pathname1):
    pathname1.touch()

    FileUtils.mkdir(pathname1)
    assert pathname1.is_dir()


def test_mkdir_mock(mocker, pathname1):
    os_path_exists = mocker.patch("os.path.exists", return_value=False)
    os_makedirs = mocker.patch("os.makedirs")

    FileUtils.mkdir(pathname1)

    os_path_exists.assert_called_once()
    os_makedirs.assert_called_once_with(pathname1)


def test_get_realpath_file(pathname1):
    file = pathname1
    file.touch()
    assert FileUtils.get_realpath(file) == str(file.resolve().parent)

    file = file / ".."
    assert FileUtils.get_realpath(file) == str(file.resolve().parent)

    file = Path("/..")
    assert FileUtils.get_realpath(file) == str(file.resolve().parent)

    file = file / "../a/b/"
    assert FileUtils.get_realpath(file) == str(file.resolve().parent)


def test_get_realpath_dir(pathname1):
    for p in [pathname1 / "..", Path("/.."), pathname1 / "../a/b/"]:
        assert FileUtils.get_realpath(p) == str(p.resolve().parent)


def test_remove_dir(pathname1):
    dir_ = pathname1
    dir_.mkdir()

    assert dir_.exists()
    FileUtils.remove_dir(dir_)
    assert not dir_.exists()


def test_remove_dir_with_noexisted_dir(pathname1):
    dir_ = pathname1

    FileUtils.remove_dir(dir_)
    assert not dir_.exists()


def test_is_exist(pathname1):
    dir_ = pathname1

    assert not FileUtils.is_exist(dir_)
    dir_.mkdir()
    assert FileUtils.is_exist(dir_)


def test_move(pathname1, pathname2):
    src = pathname1
    dst = pathname2

    src.mkdir()

    FileUtils.move_dir(src, dst)
    assert dst.exists() and not src.exists()


def test_move_nonexists(pathname1, pathname2):
    src = pathname1
    dst = pathname2

    FileUtils.move_dir(src, dst)
    assert not dst.exists() and not src.exists()


def test_read_dir(mocker, pathname1):
    entries = [".git", "some.done", "test.json.done"]
    mock_listdir = mocker.patch("os.listdir", return_value=entries)

    assert FileUtils.read_dir(pathname1) == [
        f"{pathname1}/some.done",
        f"{pathname1}/test.json.done",
    ]


def test_read_dir_with_ext(mocker, pathname1):
    entries = [
        ".git",
        "some.done",
        "test.json.done",
        "some.txt",
        "run.bat",
        "data.json",
        "other.json",
    ]
    mock_listdir = mocker.patch("os.listdir", return_value=entries)

    assert FileUtils.read_dir(pathname1, ".json") == [
        f"{pathname1}/data.json",
        f"{pathname1}/other.json",
    ]


def test_file_pointer(pathname1):
    pathname1.touch()

    f = FileUtils.file_pointer(pathname1, mode="r")
    assert isinstance(f, io.TextIOBase)
    assert f.mode == "r"
    f.close()


@pytest.mark.xfail(reason="No file", raises=FileNotFoundError)
def test_file_pointer_fail(pathname2):
    assert not pathname2.exists()
    f = FileUtils.file_pointer(pathname2, mode="r")
