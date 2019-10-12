import pytest


class TestJfrog:
    @pytest.mark.complete("jfrog ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("jfrog r", require_cmd=True)
    def test_rt(self, completion):
        assert completion == "rt"

    @pytest.mark.complete("jfrog b", require_cmd=True)
    def test_bt(self, completion):
        assert completion == "bt"

    @pytest.mark.complete("jfrog x", require_cmd=True)
    def test_xr(self, completion):
        assert completion == "xr"

    @pytest.mark.complete("jfrog m", require_cmd=True)
    def test_mc(self, completion):
        assert completion == "mc"

    @pytest.mark.complete("jfrog rt ping -", require_cmd=True)
    def test_flag(self, completion):
        assert completion
