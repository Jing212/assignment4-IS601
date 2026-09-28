"""Global configuration and fixtures for Pytest."""

import pytest
from app.calculation import CalculationFactory
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)


@pytest.fixture(autouse=True)
def reset_calculation_factory():
    """
    Fixture to reset CalculationFactory's registered calculations before each test.
    Ensures test isolation by clearing and re-registering default operations.
    """
    # Clear existing registrations
    CalculationFactory._calculations.clear()

    # Re-register the default calculations
    CalculationFactory.register_calculation('add')(AddCalculation)
    CalculationFactory.register_calculation('subtract')(SubtractCalculation)
    CalculationFactory.register_calculation('multiply')(MultiplyCalculation)
    CalculationFactory.register_calculation('divide')(DivideCalculation)