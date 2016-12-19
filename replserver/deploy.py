import sys
from string import Template
from ampy import pyboard, cli

try:
	port = "/dev/ttyUSB0"

	bootPath = 'boot.py'
	zippedPath = 'webrepl-inlined.html.gz'

	putTemplate = Template("ampy --port ${port} put ${frompath} ${topath}")
	resetTemplate = Template("ampy --port ${port} reset")

	try:
		print('Uploading the gzipped webrepl')
		sys.argv = putTemplate.substitute(
			port=port,
			frompath=zippedPath,
			topath=zippedPath
		).split()
		cli.cli()
	except SystemExit:
		pass

	try:
		print('Uploading boot.py implementing minimal webserver')
		sys.argv = putTemplate.substitute(
			port=port,
			frompath=bootPath,
			topath=bootPath
		).split()
		cli.cli()
	except SystemExit:
		pass

	try:
		print('Resetting Cockle')
		sys.argv = resetTemplate.substitute(
			port=port
		).split()
		cli.cli()
	except SystemExit:
		pass

except ampy.pyboard.PyboardError:
	print("Is " + port + " in use?")