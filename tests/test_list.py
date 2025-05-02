import pytest


class TestList:

    @pytest.mark.parametrize('arg', [-567, -1, 0, 1, 400, 'asd', '', 1.23, [1, 0], {1, 0}])
    def test_list_append(self, arg, create_list):
        lst = create_list
        lst.append(arg)
        assert arg in lst

    @pytest.mark.parametrize('arg', [-567, -1, 0, 1, 400, 'asd', '', 1.23, [1, 0], {1, 0}])
    def test_list_pop(self, arg):
        lst = [arg]
        n = lst.pop()
        assert n == arg

    def test_list_negative(self):
        lst = []
        with pytest.raises(IndexError):
            lst.pop()

