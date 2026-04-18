from validator import Instruction, VivekaRuntime
from MSPB_Trace.trace import Trace


def main():
    runtime = VivekaRuntime()
    trace = Trace()

    instructions = [
        Instruction("valid_signature", 1080.0, "task A"),
        Instruction("", 1080.0, "task B"),
        Instruction("valid_signature", 900.0, "task C"),
    ]

    for instr in instructions:
        verdict = runtime.judge(instr)
        record = trace.add_record(instr.payload, verdict)

        print(f"Instruction: {instr.payload} → {verdict}")

    print("\nTRACE:")
    trace.show_trace()


if __name__ == "__main__":
    main()
