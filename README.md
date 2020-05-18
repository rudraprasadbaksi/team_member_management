# Team Member Management

The goal of the project is to implement an HTTP API to support a team-member management
application. The team member data should be persisted in a Postgres database. The application
needs to support listing team members, adding a new team member, editing a team member,
and deleting a team member.

## Getting Started

The Project was implemented on Django using REST Framework and hosted on AWS

### Prerequisites

What things one need's to install(The versions may vary)

For the local machine following prerequisites should be installed:

```
Django==2.0.7
djangorestframework==3.11.0
psycopg2==2.8.5
pytz==2020.1
```

For the AWS hosting following prerequistes should be installed:

```
Django==2.0.7
djangorestframework==3.11.0
gunicorn==20.0.4
pkg-resources==0.0.0
psycopg2-binary==2.8.5
pytz==2020.1
```
nginx server was also installed

## Running the tests

Tests were written in the "tests.py" file in the "members" app. To run the test one can make use of the following command:
```
python manage.py test members
```

# Preparing for Deployment
few changes were made:
1. Debug = False # Done to prevent the api from leaking information
2. ALLOWED_HOSTS = ['*']

