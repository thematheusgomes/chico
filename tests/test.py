from urllib.parse import parse_qsl

url = 'token=4OGhX5a3woghS8k4wBxsyIYe&team_id=T02NV40F7&team_domain=paguemob&channel_id=G01PH9JR6DP&channel_name=privategroup&user_id=UGBF4ACES&user_name=matheus.gomes&command=%2Fcheckuser&text=hi&api_app_id=A01NPSWQ9UP&is_enterprise_install=false&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT02NV40F7%2F1788378624611%2FNjh3issyOrsCOzqUrDGyF8CY&trigger_id=1800802312817.2777136517.32487f2b0e09cd8f5d63583ec6cb8228'

print(dict(parse_qsl(url)))
