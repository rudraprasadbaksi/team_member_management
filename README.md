# Team Member Management

The goal of the project is to implement an HTTP API to support a team-member management
application. The team member data should be persisted in a Postgres database. The application
needs to support listing team members, adding a new team member, editing a team member,
and deleting a team member.

## Getting Started

The Project was implemented on Django using REST Framework and hosted on AWS

### Prerequisites

What things one need's to install(The versions may vary)

```
Django==2.0.7
djangorestframework==3.11.0
gunicorn==20.0.4
pkg-resources==0.0.0
psycopg2-binary==2.8.5
pytz==2020.1
```

## Running the tests

Tests were written in the "tests.py" file in the "members" app. To run the test one can make use of the following command:
```
python manage.py test members
```

# Preparing for Deployment

