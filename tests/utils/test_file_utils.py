from pycmmn.utils.FileUtils import FileUtils


def test_mkdir(tmp_path):
    dir_ = tmp_path / "sub"
    FileUtils.mkdir(dir_)

    assert dir_.exists()


def test_move(tmp_path):
    src = tmp_path / 'src'
    dst = tmp_path / 'dst'

    src.mkdir()

    FileUtils.move_dir(src, dst)

    assert dst.exists() and not src.exists()


def test_remove_dir(tmp_path):
    dir_ = tmp_path / 'removed'
    dir_.mkdir()

    FileUtils.remove_dir(dir_)

    assert not dir_.exists()


def test_is_exist(tmp_path):
    dir_ = tmp_path / "exist"

    assert not FileUtils.is_exist(dir_)

    dir_.mkdir()

    assert FileUtils.is_exist(dir_)
