import glob
import json

import pytest

DM_COMPONENTS_TEMPLATES_DIR = 'digitalmarketplace_frontend_jinja/templates/components'
DM_COMPONENTS_NODE_DIR = 'node_modules/ccs-digitalmarketplace-govuk-frontend/digitalmarketplace/components'


def get_components():
    paths = glob.glob(f'{DM_COMPONENTS_TEMPLATES_DIR}/*/macro.html')
    for path in paths:
        component_name = path.split('/')[3]

        yield (component_name)


def component_fixtures(component_name):
    with open(f'{DM_COMPONENTS_NODE_DIR}/{component_name}/fixtures.json') as file:
        fixtures = json.load(file)

    macro_name = component_name_to_macro_name(component_name)

    for fixture in fixtures.get('fixtures'):
        yield (macro_name, fixture['name'], fixture.get('options', {}), fixture['html'])


def components_fixtures():
    for component_name in get_components():
        for macro_name, fixture_name, fixture_options, fixture_html in component_fixtures(component_name):
            yield (component_name, macro_name, fixture_name, fixture_options, fixture_html)


def component_name_to_macro_name(component_name: str):
    return component_name.replace('-', ' ').title().replace(' ', '')


def html_to_one_line(html: str):
    return html.strip().replace("\n", '').replace(" ", '').lower()


@pytest.mark.parametrize(
    "component_name, macro_name, fixture_name, fixture_options, fixture_html",
    components_fixtures()
)
def test_render_component(client, component_name, macro_name, fixture_name, fixture_options, fixture_html):
    response = client.post(
        f'/component/{component_name}',
        content_type='application/json',
        data=json.dumps({
            'macro_name': macro_name,
            'params': fixture_options
        })
    )
    assert response.status_code == 200
    assert (
        html_to_one_line(response.get_data().decode("utf-8")) == html_to_one_line(fixture_html)
    ), f"Did not match for '{component_name}' component with example: '{fixture_name}'"


def test_all_jinja_templates_exist():
    excluded_components = ['follow-up-question-example']

    jinja_components = [component for component in get_components()]

    nunjucks_components = []

    paths = glob.glob(f'{DM_COMPONENTS_NODE_DIR}/*/macro.njk')
    for path in paths:
        component_name = path.split('/')[4]

        if component_name not in excluded_components:
            nunjucks_components.append(component_name)

    assert jinja_components == nunjucks_components


# # Debugging test case for testing one component
# @pytest.mark.parametrize("macro_name, fixture_name, fixture_options, fixture_html", component_fixtures(''))
# def test_component(client, macro_name, fixture_name, fixture_options, fixture_html):
#     component_name = ''
#     response = client.post(
#         f'/component/{component_name}',
#         content_type='application/json',
#         data=json.dumps({
#             'macro_name': macro_name,
#             'params': fixture_options
#         })
#     )
#     assert response.status_code == 200
#     assert (
#         html_to_one_line(response.get_data().decode("utf-8")) == html_to_one_line(fixture_html)
#     ), f"Did not match for '{component_name}' component with example: '{fixture_name}'"


# # Debugging test case for testing one component example
# def test_individual_component(client):
#     component_name = ''
#     macro_name = component_name_to_macro_name(component_name)
#     fixture_name = ''
#     with open(f'{DM_COMPONENTS_NODE_DIR}/{component_name}/fixtures.json') as file:
#         fixtures = json.load(file)
#         fixture = [fixture for fixture in fixtures['fixtures'] if fixture['name'] == fixture_name][0]

#     response = client.post(
#         f'/component/{component_name}',
#         content_type='application/json',
#         data=json.dumps({
#             'macro_name': macro_name,
#             'params': fixture['options']
#         })
#     )
#     assert response.status_code == 200
#     print('---TEST---')
#     print(html_to_one_line(fixture['html']))
#     print(html_to_one_line(response.get_data().decode("utf-8")))
#     assert (
#         html_to_one_line(response.get_data().decode("utf-8")) == html_to_one_line(fixture['html'])
#     ), f"Did not match for '{component_name}' component with example: '{fixture_name}'"
