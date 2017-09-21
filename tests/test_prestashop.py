import pytest


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/test01.yml")["ansible_facts"]


def test_php_fpm_service(Service):
    assert Service("php7.0-fpm").is_enabled
    assert Service("php7.0-fpm").is_running


def test_prestashop_service(Socket, AnsibleVars):
    port = AnsibleVars["prestashop_port"]

    assert Socket("unix:///run/php/php7.0-fpm.sock").is_listening
    assert Socket("tcp://0.0.0.0:" + str(port)).is_listening
