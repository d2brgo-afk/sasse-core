class Instruction:
    def __init__(self, selo_genese: str, vetor_simetria: float, payload: str):
        self.selo_genese = selo_genese
        self.vetor_simetria = vetor_simetria
        self.payload = payload


class VivekaRuntime:
    SIMETRIA_PERFEITA = 1080.0

    def validate_sdb(self, instruction: Instruction) -> bool:
        """
        Validação estrutural básica.
        """
        if not instruction.selo_genese:
            return False

        if instruction.vetor_simetria != self.SIMETRIA_PERFEITA:
            return False

        return True

    def judge(self, instruction: Instruction) -> str:
        """
        Julgamento simples: REAL ou IRREAL.
        """
        if not self.validate_sdb(instruction):
            return "IRREAL"

        if not instruction.payload:
            return "IRREAL"

        return "REAL"


if __name__ == "__main__":
    instr = Instruction(
        selo_genese="valid_signature",
        vetor_simetria=1080.0,
        payload="execute"
    )

    runtime = VivekaRuntime()
    result = runtime.judge(instr)

    print(f"Verdict: {result}")
