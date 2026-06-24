from __future__ import annotations

from datetime import date, time
from enum import Enum
from typing import List, Optional


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(Enum):
    PENDING = "pending"
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    SKIPPED = "skipped"


class Pet:
    def __init__(
        self,
        name: str = "",
        species: str = "",
        breed: str = "",
        age: int = 0,
        allowed_foods: Optional[List[str]] = None,
        restricted_foods: Optional[List[str]] = None,
        medical_history: str = "",
    ) -> None:
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.allowed_foods = allowed_foods if allowed_foods is not None else []
        self.restricted_foods = restricted_foods if restricted_foods is not None else []
        self.medical_history = medical_history
        self._care_requirements: List[PetNeeds] = []
        self._tasks: List[Task] = []

    def update_profile(self, name: str, species: str, breed: str, age: int) -> None:
        pass

    def set_dietary_restrictions(
        self, allowed: List[str], restricted: List[str]
    ) -> None:
        pass

    def update_medical_history(self, history: str) -> None:
        pass

    def get_care_requirements(self) -> List[PetNeeds]:
        pass


class OwnerAvailability:
    def __init__(
        self,
        owner_name: str = "",
        available_times: Optional[List[TimeSlot]] = None,
        priority_preferences: Optional[List[str]] = None,
    ) -> None:
        self.owner_name = owner_name
        self.available_times = available_times if available_times is not None else []
        self.priority_preferences = (
            priority_preferences if priority_preferences is not None else []
        )

    def add_available_time(self, start_time: time, end_time: time) -> None:
        pass

    def remove_available_time(self, slot_id: str) -> None:
        pass

    def set_priority_preferences(self, priorities: List[str]) -> None:
        pass

    def get_available_times(self) -> List[TimeSlot]:
        pass

    def generate_schedule_options(
        self, pet: Pet, needs: List[PetNeeds], tasks: List[Task]
    ) -> List[DailySchedule]:
        pass

    def edit_schedule(
        self, schedule: DailySchedule, task_id: str, new_start_time: time
    ) -> DailySchedule:
        pass

    def explain_schedule(self, schedule: DailySchedule) -> str:
        pass


class PetNeeds:
    def __init__(
        self,
        need_type: str = "",
        description: str = "",
        frequency: str = "",
        is_required: bool = True,
        minimum_priority: Priority = Priority.MEDIUM,
    ) -> None:
        self.need_type = need_type
        self.description = description
        self.frequency = frequency
        self.is_required = is_required
        self.minimum_priority = minimum_priority

    def add_need(self, need_type: str, description: str, frequency: str) -> None:
        pass

    def update_need(self, need_type: str, description: str, frequency: str) -> None:
        pass

    def to_tasks(self) -> List[Task]:
        pass


class Task:
    def __init__(
        self,
        task_id: str = "",
        title: str = "",
        duration_minutes: int = 0,
        priority: Priority = Priority.MEDIUM,
        category: str = "",
        status: TaskStatus = TaskStatus.PENDING,
        scheduled_start_time: Optional[time] = None,
    ) -> None:
        self.task_id = task_id
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.category = category
        self.status = status
        self.scheduled_start_time = scheduled_start_time

    def create_task(
        self, title: str, duration: int, priority: Priority, category: str
    ) -> None:
        pass

    def update_task(self, title: str, duration: int, priority: Priority) -> None:
        pass

    def reschedule(self, new_start_time: time) -> None:
        pass

    def mark_complete(self) -> None:
        pass

    def is_scheduled(self) -> bool:
        pass


class TimeSlot:
    def __init__(
        self,
        slot_id: str = "",
        start_time: Optional[time] = None,
        end_time: Optional[time] = None,
    ) -> None:
        self.slot_id = slot_id
        self.start_time = start_time
        self.end_time = end_time

    def fits(self, duration_minutes: int) -> bool:
        pass

    def overlaps(self, other: TimeSlot) -> bool:
        pass


class DailySchedule:
    def __init__(
        self,
        schedule_id: str = "",
        schedule_date: Optional[date] = None,
        scheduled_tasks: Optional[List[Task]] = None,
        unscheduled_tasks: Optional[List[Task]] = None,
        explanation: str = "",
    ) -> None:
        self.schedule_id = schedule_id
        self.date = schedule_date
        self.scheduled_tasks = (
            scheduled_tasks if scheduled_tasks is not None else []
        )
        self.unscheduled_tasks = (
            unscheduled_tasks if unscheduled_tasks is not None else []
        )
        self.explanation = explanation

    def add_task(self, task: Task, start_time: time) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass

    def move_task(self, task_id: str, new_start_time: time) -> None:
        pass

    def get_tasks_by_time(self) -> List[Task]:
        pass
