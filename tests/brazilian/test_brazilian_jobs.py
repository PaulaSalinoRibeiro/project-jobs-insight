from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_translet_mock = {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
    dict_translet = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    print(dict_translet)
    assert dict_translet_mock in dict_translet
