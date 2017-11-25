# NETWORK UTILITIES

def internetStatus():
	"""
	Delivers a summary of the internet connectivity of the system.

	Returns:
		feedbackOutput (str): Resulting feedback.
		internetStatus (bool): Represents the internet connectivity of the system.
	"""
	consoleOutput = doConsoleCommand(constants.internetCheck)

	# Parse output for results
	status = False
	feedbackOutput = constants.internetCheckFailed

	if "unknown" not in consoleOutput and "failure" not in consoleOutput:
		splitOutput = re.split(",", consoleOutput)

		if "0" not in splitOutput[1]:
			status = True
			ipAddress = doConsoleCommand(constants.getInternetIP)
			feedbackOutput = constants.internetCheckPassed.format(ipAddress)

	return feedbackOutput, status


def restartModem():
	"""
	Restarts the modem network interface.

	Returns:
		feedbackOutput (str): Resulting feedback.
	"""
	consoleOutput = doConsoleCommand(constants.restartModem)

	# Parse output for results
	feedbackOutput = constants.modemRestartFailed

	if "SUCCESS" in consoleOutput:
		feedbackOutput = constants.modemRestartPassed

	return feedbackOutput


def restartVPN():
	"""
	Restarts the system's VPN daemon.

	Returns:
		feedbackOutput (str): Resulting feedback.
	"""
	consoleOutput = doConsoleCommand(constants.restartVPN)

	# Parse output for results
	feedbackOutput = constants.vpnRestartFailed

	if "SUCCESS" in consoleOutput:
		feedbackOutput = constants.vpnRestartPassed

	return feedbackOutput


def vpnStatus():
	"""
	Delivers a summary of the VPN connectivity of the system.

	Returns:
		feedbackOutput (str): Resulting feedback.
		vpnStatus (bool): Represents the VPN connectivity of the system.
	"""
	consoleOutput = doConsoleCommand(constants.vpnCheck)

	# Parse output for results
	status = False
	feedbackOutput = constants.vpnCheckFailed

	if "0" not in re.split(",", consoleOutput)[1]:
		status = True
		ipAddress = doConsoleCommand(constants.getVpnIP)
		feedbackOutput = constants.vpnCheckPassed.format(ipAddress)

	return feedbackOutput, status