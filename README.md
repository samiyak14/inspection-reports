# Inspection Reports

A personal learning project built with the Frappe Framework to practise application development, Git workflows, and report generation.

## Project Overview

Inspection Reports is a practice application for managing fictional industrial equipment inspections and generating structured inspection reports.

This project is intended for learning and portfolio purposes. It uses fictional data and illustrative inspection rules.

## Planned Features

- Equipment record management
- Inspection record creation and tracking
- Recording inspection readings and findings
- Illustrative inspection status and validation
- Inspection report generation
- Review and approval workflow

## Tech Stack

- **Framework:** Frappe Framework
- **Language:** Python
- **Database:** MariaDB
- **Version Control:** Git and GitHub

## Development Status

**Current stage:** Initial application setup.

Features will be implemented incrementally as part of the learning process.

## Installation

From your Frappe bench directory:

```bash
bench get-app https://github.com/samiyak14/inspection-reports.git --branch develop
bench --site your-site-name install-app inspection_reports
```

Replace `your-site-name` with the name of your Frappe site.

## Contributing

This is primarily a personal learning project. Suggestions and feedback are welcome.

The repository uses pre-commit tooling for code formatting and linting. To set it up:

```bash
cd apps/inspection_reports
pre-commit install
```

Configured tools include Ruff, ESLint, Prettier, and pyupgrade.

## License

MIT
