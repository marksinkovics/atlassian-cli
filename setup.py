""" Declaration for pip """

from setuptools import setup, find_packages

try:
    from pip._internal.download import PipSession
except ImportError:
    from pip.download import PipSession

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

from atlassian_cli.metadata import APPLICATION_VERSION

from atlassian_cli import (
    JIRA_CLI_PROG,
    BITBUCKET_CLI_PROG
)

def parse_requirements_file(requirements_path):
    """ Parser requirements file """
    install_reqs = parse_requirements(requirements_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs

setup(
    name='atlassian-cli',
    version=APPLICATION_VERSION,
    description='Command line interface for Atlassian tools',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    url='',
    license='BSD',
    author='Mark Sinkovics',
    author_email='sinkovics.mark@gmail.com',
    entry_points={
        'console_scripts': [
            '{} = atlassian_cli.jira_cli:main'.format(JIRA_CLI_PROG),
            '{} = atlassian_cli.bitbucket_cli:main'.format(BITBUCKET_CLI_PROG)
        ]
    },
    setup_requires=['pytest-runner'],
    install_requires=parse_requirements_file('requirements.txt'),
    tests_require=parse_requirements_file('requirements-dev.txt')
)
