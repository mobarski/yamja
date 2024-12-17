# Yamja

Flexible YAML configuration with Jinja2 superpowers 

## Features

- Load and merge YAML configuration files
- Use Jinja2 templates within your configuration
- Support for nested configuration lookups using dot notation
- Include and merge multiple configuration files
- Built-in support for macros
- Default configuration paths support

## Installation

```bash
pip install yamja
```

## Usage

### Basic Configuration Loading

```python
from yamja import load_config

# Load a single configuration file
config = load_config('config.yaml')

# Access values using dot notation
value = config.lookup('section.subsection.key')

# Access with default value
value = config.lookup('section.subsection.key', default='fallback')
```

### Template Rendering

```yaml
# config.yaml
templates:
  greeting: "Hello {{ name }}!"
  macros: |
    {% macro format_list(items) %}
    {% for item in items %}
    - {{ item }}
    {% endfor %}
    {% endmacro %}
```

```python
# Render a template with variables
greeting = config.render('greeting', name='World')

# Use macros in your templates
items = config.render('list_template', items=['apple', 'banana', 'orange'])
```

### Multiple Configurations

```python
from yamja import load_configs, merge_configs

# Load multiple config files
configs = load_configs(['base.yaml', 'override.yaml'])

# Merge them with later configs taking precedence
merged = merge_configs(configs)
```

### Including Other Config Files

```yaml
# main.yaml
include:
  - common.yaml
  - specific.yaml

additional_settings:
  key: value
```

## Requirements

- Python >= 3.13
- Jinja2 >= 3.1.4
- PyYAML >= 6.0.2

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- [GitHub Repository](https://github.com/mobarski/yamja)

