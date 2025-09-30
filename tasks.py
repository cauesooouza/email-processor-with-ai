from invoke import task


@task
def run(c):
    c.run("python main.py")

@task
def test(c):
    c.run("python -m unittest discover -s test")
