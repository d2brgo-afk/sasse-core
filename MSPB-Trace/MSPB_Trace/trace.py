import hashlib
import time


class TraceRecord:
    def __init__(self, parent_id: str, payload: str, verdict: str):
        self.parent_id = parent_id
        self.payload = payload
        self.verdict = verdict
        self.timestamp = int(time.time())

        self.id = self.generate_id()

    def generate_id(self) -> str:
        raw = f"{self.parent_id}{self.payload}{self.verdict}{self.timestamp}"
        return hashlib.sha256(raw.encode()).hexdigest()


class Trace:
    def __init__(self):
        self.records = []

    def add_record(self, payload: str, verdict: str):
        parent_id = self.records[-1].id if self.records else "GENESIS"

        record = TraceRecord(parent_id, payload, verdict)
        self.records.append(record)

        return record

    def show_trace(self):
        for r in self.records:
            print(f"{r.id[:8]} | {r.verdict} | {r.payload} | parent: {r.parent_id[:8]}")


if __name__ == "__main__":
    trace = Trace()

    r1 = trace.add_record("execute A", "REAL")
    r2 = trace.add_record("execute B", "IRREAL")

    trace.show_trace()
