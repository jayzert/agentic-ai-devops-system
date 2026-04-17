def analyze_logs(log):
    if "ModuleNotFoundError" in log:
        return "Missing dependency detected (install required package)"
    elif "Failed tests" in log:
        return "Test failures detected"
    else:
        return "Unknown error"