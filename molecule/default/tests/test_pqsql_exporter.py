import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service(host):
    service = host.service("postgres_exporter")
    assert service.is_enabled
    assert service.is_running
