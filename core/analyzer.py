"""
Analyzer Engine.

Analyze a TaskRequest and produce a TaskProfile.
"""

from domain import TaskProfile, TaskRequest
from domain.profile import TaskComplexity, TaskSize
from domain.task import QualityLevel


SMALL_TASK_LIMIT = 8_000
MEDIUM_TASK_LIMIT = 64_000


class Analyzer:
    """Analyze incoming tasks."""

    def analyze(self, request: TaskRequest) -> TaskProfile:
        """Convert TaskRequest into TaskProfile."""

        total_tokens = (
            request.estimated_input_tokens
            + request.estimated_output_tokens
        )

        size = self._determine_size(total_tokens)

        complexity = self._determine_complexity(request.quality)

        return TaskProfile(
            task=request.task,
            total_tokens=total_tokens,
            size=size,
            complexity=complexity,
            budget=request.budget,
            quality=request.quality,
            latency=request.latency,
        )

    @staticmethod
    def _determine_size(total_tokens: int) -> TaskSize:
        """Determine task size."""

        if total_tokens < SMALL_TASK_LIMIT:
            return TaskSize.SMALL

        if total_tokens < MEDIUM_TASK_LIMIT:
            return TaskSize.MEDIUM

        return TaskSize.LARGE

    @staticmethod
    def _determine_complexity(
        quality: QualityLevel,
    ) -> TaskComplexity:
        """Determine task complexity."""

        if quality == QualityLevel.HIGH:
            return TaskComplexity.HIGH

        if quality == QualityLevel.MEDIUM:
            return TaskComplexity.MEDIUM

        return TaskComplexity.LOW