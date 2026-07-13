class CapabilityEngine:

    def supports(
        self,
        model: str,
        capability: str,
    ) -> bool:
        ...

    def has_strength(
        self,
        model: str,
        task: str,
    ) -> bool:
        ...

    def context_window(
        self,
        model: str,
    ) -> int:
        ...

    def max_output_tokens(
        self,
        model: str,
    ) -> int:
        ...