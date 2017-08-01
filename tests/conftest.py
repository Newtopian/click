from click.testing import CliRunner

import pytest


@pytest.fixture(scope='function')
def runner(request):
    return CliRunner()


if __name__ == '__main__':
    import pytest
    pytest.main()