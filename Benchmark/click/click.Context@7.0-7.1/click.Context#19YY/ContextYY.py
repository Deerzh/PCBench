import click
command = click.Command('my_command')
context = click.Context(command, parent=None, info_name=None, obj=None, auto_envvar_prefix=None)
