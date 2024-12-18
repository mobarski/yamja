import yaml


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def test_load_first():
    data = load_yaml('tests/data/load_first.yaml')
    assert data['title'] == 'First Test Note'
    assert 'test' in data['tags']
    assert 'first' in data['tags']
    assert data['created'].year == 2024
    assert data['created'].month == 1
    assert data['created'].day == 1
    assert 'content' in data
    assert len(data['content'].strip().split('\n')) > 1


def test_load_second():
    data = load_yaml('tests/data/load_second.yaml')
    assert data['title'] == 'Second Test Note'
    assert 'test' in data['tags']
    assert 'second' in data['tags']
    assert data['created'].year == 2024
    assert data['created'].month == 1
    assert data['created'].day == 2
    assert 'content' in data
    assert any(line.strip().startswith('-') for line in data['content'].split('\n'))


def test_load_both():
    first = load_yaml('tests/data/load_first.yaml')
    second = load_yaml('tests/data/load_second.yaml')
    assert first['title'] != second['title']
    assert 'test' in first['tags'] and 'test' in second['tags']
    assert first['created'] < second['created']
