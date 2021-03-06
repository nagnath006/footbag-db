"""Uses pyinvoke to do common tasks"""

from invoke import task, run

@task
def compile_scss():
    """Compile the SCSS and copy to relevant static directory"""
    run("mkdir -p ./static/basic_theme/css/")
    run("mkdir -p ./footbag_site/static/basic_theme/css/")
    run("pyscss ./scss/*.scss > ./static/basic_theme/css/style.css")
    run("cp ./static/basic_theme/css/style.css ./footbag_site/static/basic_theme/css/style.css")

@task
def run_tests():
    """Run the unit testing suite"""
    run("python manage.py test")

@task
def restart_server():
    """The command to restart the web server.
    PythonAnywhere is set up such that touching the WSGI file restarts the server.
    Change this command to whatever the web server requires."""
    run('touch /var/www/www_footbag_info_wsgi.py')#restarts PythonAnywhere server


@task(run_tests)
def stage_changes(branch):
    """
    Prepare to stage changes on the staging server from a git branch if and only
    if the unit tests pass.
    The syntax to call this from the command line is:

    >>> invoke stage_changes --branch=foo_branch

    where branch_name is the name of the branch being deployed
    """
    run('git checkout develop && git merge --no-ff ' + branch)
    run('python manage.py migrate footbagmoves')

@task(run_tests)
def prepare_deployment():
    """
    Prepare to deploy from develop to master and only if the unit tests pass
    The syntax to call this from the command line is:

    >>> invoke prepare_deployment

    """
    run('git checkout master && git merge develop')

@task(post=[restart_server])
def deploy_to_live():
    """
    Deploy from the dev folder to the live site using git, assumes changes have
    already been prepared with prepare_deployment.
    """
    import os
    pwd = os.getcwd()
    os.chdir('/home/janis/footbagsite/www_footbag_info/')
    compile_scss()
    run('git checkout master')
    run('git pull /home/janis/footbagsite/dev-site/ master')
    run('python manage.py migrate footbagmoves')
    os.chdir(pwd)

@task
def create_search_index():
    """Create the index files needed to run Haystack search"""
    run('python manage.py update_index')
