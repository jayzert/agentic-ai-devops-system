def check_pod_status(status):
    if status == "CrashLoopBackOff":
        return "Container failing to start. Check environment variables or startup command."
    elif status == "ImagePullBackOff":
        return "Image cannot be pulled. Check container registry."
    else:
        return "Pod running normally"