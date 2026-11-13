"""Public intake UI for Quillharbor Legal Ops"""

class MatterIntake:
    """Internal service for matter-intake."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(MatterIntake().status())
