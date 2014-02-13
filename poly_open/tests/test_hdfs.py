
from pytest import monkeypatch
import poly_open

class MockHDFS(object):
    open_called = False
    ls_called = False
    rename_called = False
    mkdir_called = False
    makedirs_called = False
    rmtree_called = False
    #cp_called = False

    def ls(self, *args, **kwargs):
        pass

    def open(self, *args, **kwargs):
        pass
    
    def ... halted development here.

def test_hdfs(monkeypatch):
    mock_hdfs = MockHDFS()
    monkeypatch.setattr(pydoop, 'hdfs', mock_hdfs)

    open('foo')
    assert mock_hdfs.open_called

    os.listdir('foo')
    assert mock_hdfs.ls_called

    os.rename('foo')
    assert mock_hdfs.rename_called

    os.mkdir('foo')
    assert mock_hdfs.mkdir_called

    os.makedirs('foo/bar/baz')
    assert mock_hdfs.makedirs_called

    shutils.rmtree('foo/bar/baz')
    assert mock_hdfs.rmtree_called

