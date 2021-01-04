entities = {
    'v2/alerts': [
        '{entity}/{id}',
    ],
    'v1/incidents': [
        '{entity}/{id}',
        '{entity}/{id}/logs',
        '{entity}/{id}/notes',
    ],
    'v2/integrations': [
        '{entity}/{id}',
        '{entity}/{id}/actions',
    ],
    'v2/heartbeats': None,
    'v2/policies/alert': [
        'v2/policies/{id}',
    ],
    'v1/maintenance': [
        '{entity}/{id}',
    ],
    'v2/account': None,
    'v2/users': [
        '{entity}/{id}',
        '{entity}/{id}/contacts',
        '{entity}/{id}/escalations',
        '{entity}/{id}/teams',
        '{entity}/{id}/forwarding-rules',
        '{entity}/{id}/schedules',
        '{entity}/{id}/notification-rules',
    ],
    'v2/users/saved-searches': [
        '{entity}/{id}',
    ],
    'v2/roles': [
        '{entity}/{id}',
    ],
    'v2/teams': [
        '{entity}/{id}',
        '{entity}/{id}/logs',
        '{entity}/{id}/roles',
        '{entity}/{id}/routing-rules',
    ],
    'v2/schedules': [
        '{entity}/{id}',
        '{entity}/{id}/timeline',
        '{entity}/{id}/rotations',
        '{entity}/{id}/overrides',
        '{entity}/{id}/on-calls',
    ],
    'v2/escalations': [
        '{entity}/{id}',
    ],
    'v2/forwarding-rules': [
        '{entity}/{id}',
    ],
    'v1/services': [
        '{entity}/{id}',
        '{entity}/{id}/incident-rules',
        '{entity}/{id}/incident-templates',
        '{entity}/{id}/audience-templates',
    ],
    'v1/incident-templates': None,
}
