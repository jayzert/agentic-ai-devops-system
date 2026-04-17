from tools.log_analyzer import analyze_logs
from tools.k8s_checker import check_pod_status

def agent(log, pod_status):
    print("[Planning] Deciding what to analyse...")

    print("[Tool] Analysing CI/CD logs...")
    log_result = analyze_logs(log)

    print("[Tool] Checking Kubernetes pod status...")
    pod_result = check_pod_status(pod_status)

    print("[Reflection] Verifying results...")

    return f"""
FINAL DIAGNOSIS:
- Log Issue: {log_result}
- Pod Issue: {pod_result}
"""

if __name__ == "__main__":
    sample_log = "ModuleNotFoundError: No module named 'requests'"
    sample_pod_status = "CrashLoopBackOff"

    result = agent(sample_log, sample_pod_status)
    print(result)