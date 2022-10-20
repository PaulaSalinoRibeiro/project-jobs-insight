from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_translet_mock = {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }

    assert dict_translet_mock in read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
    )
