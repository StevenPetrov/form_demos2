from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_text(text):
    if '_' in text:
        raise ValidationError('dont use symbols')


def validate_days(value):
    if value < 1 or 10 < value:
        raise ValidationError('must be between 1 and 10')


@deconstructible
class ValueInRangeValidator():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __call__(self, value):
        if value < self.min or self.max < value:
            raise ValidationError('Value Error XXXXXXXX')

    def __eq__(self, other):
        return (
                isinstance(other, ValueInRangeValidator)
                and self.min == other.min and self.max == self.min
        )


def validate_max_todos(assignee):
    if assignee.todo_set.count() >= assignee.MAX_TASKS:
        raise ValidationError(f'{assignee} он не мое повече да бачка')
