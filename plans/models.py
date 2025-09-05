from djmoney.models.fields import MoneyField
from django.db import models


class PlanType(models.TextChoices):
    """
    The type of plan.
    """
    PLAN_PERSONALIZED_COACHING = "PLAN_PERSONALIZED_COACHING", "Personalized Coaching"
    PLAN_TWELVE_WEEK_MARATHON = (
        "PLAN_TWELVE_WEEK_MARATHON",
        "12-Week Marathon Training",
    )
    PLAN_STRENGTH_COACHING = ("PLAN_STRENGTH_COACHING", "Strength Programming")


class PricingStrategy(models.TextChoices):
    """
    The strategy for pricing a plan.
    """
    PRICING_STRATEGY_MONTHLY = "PRICING_STRATEGY_MONTHLY", "Priced per month"
    PRICING_STRATEGY_ONE_TIME = "PRICING_STRATEGY_ONE_TIME", "Purchased once"


class Plan(models.Model):
    """
    A Plan is a program that a client can enroll in.
    """
    plan_type = models.CharField(
        max_length=50,
        choices=PlanType.choices,
        default=PlanType.PLAN_PERSONALIZED_COACHING,
    )
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency="USD",
        max_digits=5,
    )
    pricing_strategy = models.CharField(
        max_length=50,
        choices=PricingStrategy.choices,
        default=PricingStrategy.PRICING_STRATEGY_MONTHLY,
    )
    description = models.TextField(blank=True)
    key_features = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Plan: {self.plan_type}"
