# Ansible PostgreSQL exporter
Installs the PostgreSQL Exporter for Prometheus.

## Descriptions
This role install PostgreSQL exporter in `prometheus_exporter_dir` directory. Full path to binary will be like this one: `/opt/prometheus/exporters/postgres_exporter-0.10.1.linux-amd64/`. Then create soft link from directory with binary to `prometheus_exporter_dir directory. Systemd use this link to start exporter.

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `postgres_exporter_user` | User to start postgres_exporter.  | `postgres` |
| `postgres_exporter_version`| Version of the exporter to use | `0.10.1` |
| `postgres_exporter_checksum` | SHA256 checksum | 5344afe06a90c3cbd52803d56031bfcbcff78b56448e16c9228697ea0a2577b7 |
| `prometheus_exporter_dir` | Directory for prometheus exporters | `/opt/prometheus/exporters` |
| `postgres_exporter_config_file` | Configuration parameters file for postgres_exporter | `/etc/default/postgres_exporter` |
| `postgres_exporter_queries` | File with PostgreSQL metrics queries. Default [guery file](./files/queries.yml) | `queries.yml` |
| `postgres_exporter_query_dir` | Direcroty for postgres_exporter query file| `/etc/postgres_exporter` |
| `postgres_exporter_log_path` | Directory for postgres_exporter logs |
| `postgres_exporter_data_source_name` | [DATA_SOURCE_NAME](https://github.com/prometheus-community/postgres_exporter#environment-variables) ENV definition | `user=postgres host=/var/run/postgresql/ sslmode=disable` |
| `postgres_exporter_flags`| Array of exporter [flags](https://github.com/prometheus-community/postgres_exporter#flags) | ['--auto-discover-databases', '--extend.query-path={{ postgres_exporter_query_dir }}/queries.yml'] |

## Example Playbook
```yaml
- hosts: all
  roles:
    - artem_shestakov.postgres_exporter
```

## License
GPLv3

## Author Information
artem.s.shestakov@gmail.com
