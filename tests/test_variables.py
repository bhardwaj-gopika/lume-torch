from lume_torch.variables import ScalarVariable, get_variable


def test_get_variable():
    var = get_variable(ScalarVariable.__name__)(name="test")
    assert isinstance(var, ScalarVariable)
