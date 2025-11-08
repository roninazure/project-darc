import json
import sys
import datetime

INPUT_FILE = "mirage/infra_indicators.txt"
LOG_FILE = "mad-log/mirage_scan_" + datetime.datetime.utcnow().strftime("%Y-%m-%d") + ".json"

def load_indicators():
    with open(INPUT_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def run_trace_probe():
    indicators = load_indicators()
    simulated_results = []

    for ind in indicators:
        result = {
            "indicator": ind,
            "llm_trace": any(kw in ind.lower() for kw in ["key", "token", "password", "secret"]),
            "hallucination": any(kw in ind.lower() for kw in ["sandbox", "dev", "test"]),
            "time": datetime.datetime.utcnow().isoformat() + "Z"
        }
        simulated_results.append(result)

    with open(LOG_FILE, "w") as f:
        json.dump(simulated_results, f, indent=2)

    for r in simulated_results:
        print(json.dumps(r))

if __name__ == "__main__":
    run_trace_probe()
