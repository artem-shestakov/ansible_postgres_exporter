from enum import auto
from urllib import request
import testinfra.utils.ansible_runner
import os
import pytest
import requests

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service(host):
    service = host.service("postgres_exporter")
    assert service.is_enabled
    assert service.is_running

def test_port(host):
    assert host.socket("tcp://9187").is_listening

def test_metrics(host):
    output = host.check_output("/bin/bash -c 'exec 3<>/dev/tcp/127.0.0.1/9187 && echo -e \"GET /metrics HTTP/1.1\r\nhost: 127.0.0.1\r\nConnection: close\r\n\r\n\" >&3 && cat <&3'")
    assert "pg_up 1" in output